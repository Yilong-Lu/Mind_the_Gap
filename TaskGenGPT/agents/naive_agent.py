import os
import random
from jinja2 import Template
from typing import Annotated, List, Sequence
from typing_extensions import TypedDict
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from datetime import datetime
from tqdm import tqdm

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from response_models import TasksReport
from scenes import get_all_scene_settings

def prepare_agent(llm: AzureChatOpenAI):
    generate_sys_prompt = open("./prompts/generate_sys.txt").read()
    generate_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                generate_sys_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    task_generator = generate_prompt | llm
    return task_generator


def generate_and_save_tasks(scene_settings, num_runs_per_scene):
    results = []
    for scene_name, items_list in tqdm(scene_settings.items(), desc="Processing scenes"):
        
        for run_idx in tqdm(range(num_runs_per_scene), desc=f"Runs for {scene_name}", leave=False):
            print(f"Processing {scene_name} - Run {run_idx + 1}/{num_runs_per_scene}")

            # inplace shuffle
            random.shuffle(items_list)    

            resp = task_generator.invoke({'messages': [
                HumanMessage(content=generate_task_prompt.render(
                    scene=items_list, 
                    examples=examples
                ))
            ]})
            structure_resp = llm.with_structured_output(TasksReport).invoke(resp.content)
            

            print(f"Generated tasks: {len(structure_resp.tasks)}")
            for task in structure_resp.tasks:
                result_dict = {
                    'scene': scene_name,
                    'shuffled': True,
                    'run_index': run_idx + 1,
                    'model_name': llm.model_name,
                    'temperature': llm.temperature,
                    'agent': 'naive', 
                    **task.dict(),
                    'raw_response': resp.content,
                }
                results.append(result_dict)
    

    df = pd.DataFrame(results)
    output_file = f'task_generation_results_{llm.model_name}_{num_runs_per_scene}_{datetime.now().strftime("%Y%m%d_%H%M")}.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\nResults saved to {output_file}")
    
    return df, output_file

if __name__ == "__main__":

    assert load_dotenv(find_dotenv(filename=".env"))

    num_runs_per_scene = 30

    model_id = "gpt-4o-2024-08-06"
    # model_id = "gpt-4o-mini-2024-07-18"
    

    region = 'eastus'
    llm = AzureChatOpenAI(
        model=model_id,
        temperature=1.0,
        api_version=os.getenv("AI_API_VERSION"),
        api_key=os.getenv("AI_OAI_API_KEY"),
        azure_endpoint=f'{os.getenv("AI_API_BASE")}/{region}',
    )

    task_generator = prepare_agent(llm)
    
    generate_task_prompt = Template(open("./prompts/generate.txt").read())
    examples = open('./prompts/examples.txt').read()


    scene_settings = get_all_scene_settings()
    
    # one agent call: 15s
    df, output_file = generate_and_save_tasks(scene_settings, num_runs_per_scene)
