import os
import random
from jinja2 import Template
from typing import Annotated, List, Sequence
from typing_extensions import TypedDict
from dotenv import load_dotenv, find_dotenv
from tqdm import tqdm
from datetime import datetime
import pandas as pd

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from scenes import get_all_scene_settings
from response_models import TasksReport

def prepare_agents(llm):
    generate_sys_prompt = open("./prompts/generate_sys.txt").read()

    generate_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                generate_sys_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    generator = generate_prompt | llm

    reflect_sys_prompt = open("./prompts/reflect_sys.txt").read()
    reflect_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                reflect_sys_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    reflector = reflect_prompt | llm
    return generator, reflector

class State(TypedDict):
    scene_description: str
    messages: Annotated[list, add_messages]

def generation_node(state: State) -> State:
    return {"messages": [generator.invoke(state["messages"])]}

def reflection_node(state: State) -> State:
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    translated = [state["messages"][0]] + [
        cls_map[msg.type](content=msg.content) for msg in state["messages"][1:]
    ]
    res = reflector.invoke(translated)
    return {"messages": [HumanMessage(content=res.content)]}


def construct_graph():
    builder = StateGraph(State)
    builder.add_node("task_generate", generation_node)
    builder.add_node("reflect", reflection_node)
    builder.add_edge(START, "task_generate")

    def should_continue(state: State):
        if len(state["messages"]) > 6:
            # End after 3 iterations
            return END
        return "reflect"

    builder.add_conditional_edges("task_generate", should_continue)
    builder.add_edge("reflect", "task_generate")
    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)
    return graph

def generate_and_save_tasks(scene_settings, num_runs_per_scene):
    results = []
        
    for scene_name, items_list in tqdm(scene_settings.items(), desc="Processing scenes"):
        
        for run_idx in tqdm(range(num_runs_per_scene), desc=f"Runs for {scene_name}", leave=False):
            print(f"Processing {scene_name} - Run {run_idx + 1}/{num_runs_per_scene}")

            # inplace shuffle
            random.shuffle(items_list)    

            resp = graph.invoke({'messages': [
                    HumanMessage(content=generate_task_prompt.render(
                        scene=items_list, 
                        examples=examples
                    ))
                ], 'scene_description': items_list}, 
            config=config)
            
            structure_resp = llm.with_structured_output(TasksReport).invoke(resp['messages'][-1].content)
            
            for task in structure_resp.tasks:
                
                result_dict = {
                    'scene': scene_name,
                    'shuffled': True,
                    'run_index': run_idx + 1,
                    'model_name': llm.model_name,
                    'temperature': llm.temperature,
                    'agent': 'reflexion',
                    **task.dict(),
                    'raw_response': resp['messages'][-1].content,
                }
                results.append(result_dict)

    df = pd.DataFrame(results)
    output_file = f'task_generation_results_{num_runs_per_scene}_{datetime.now().strftime("%Y%m%d_%H%M")}.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\nResults saved to {output_file}")
    
    return df, output_file


if __name__ == "__main__":

    assert load_dotenv(find_dotenv(filename=".env"))

    model_id = "gpt-4o-2024-08-06"
    region = 'eastus'
    llm = AzureChatOpenAI(
        model=model_id,
        temperature=1.,
        api_version=os.getenv("AI_API_VERSION"),
        api_key=os.getenv("AI_OAI_API_KEY"),
        azure_endpoint=f'{os.getenv("AI_API_BASE")}/{region}',
    )

    generator, reflector = prepare_agents(llm)

    graph = construct_graph()

    # image_data = graph.get_graph().draw_mermaid_png()
    # with open('./figs/reflexion_agent.png', 'wb') as file:
    #     file.write(image_data)

    generate_task_prompt = Template(open("./prompts/generate.txt").read())

    examples = open('./prompts/examples.txt').read()

    config = {"configurable": {"thread_id": "1"}}
    

    scene_settings = get_all_scene_settings()

    num_runs_per_scene = 1  
    
    df, output_file = generate_and_save_tasks(scene_settings, num_runs_per_scene)