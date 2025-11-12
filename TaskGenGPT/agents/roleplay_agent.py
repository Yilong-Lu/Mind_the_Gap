import os
import random
from telnetlib import TLS
from jinja2 import Template
from typing import Annotated, List, Sequence
from typing_extensions import TypedDict
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from datetime import datetime
from tqdm import tqdm
from pydantic import BaseModel

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from response_models import TasksReport, RequiredItems
from scenes import get_all_scene_settings_align

ENERGY_DICT = {
    1: "Little energy or motivation to do much of anything", 
    2: "Enough energy to get by but not enough to be very productive", 
    3: "Typical energy level with usual productivity", 
    4: "Plenty of energy to be even more productive than usual", 
    5: "Unusually high energy feeling hyper or even agitated at times",
}

def prepare_agent(llm: AzureChatOpenAI):
    generate_sys_prompt = open("./prompts/roleplay/generate_sys.txt").read()
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


def gen_and_save_align_human_traits(scene_settings):
    results = []
    raw_ind_diff_df = pd.read_csv('./raw/individual_difference.csv')
    failed_pids = []

    for idx, row in tqdm(raw_ind_diff_df.iterrows(), desc="Processing individual difference"):
        prolific_pid = row['PROLIFIC_PID']

        n_tasks = row['nTask']
        user_setting = row['userSetting']

        self_transcendence = row['Self-Transcendence']
        self_enhancement = row['Self-Enhancement']
        openness_to_change = row['Openness to change']
        openness_vs_conservation =( 7+row['Openness to change']-row['Conservation'])/2
        enhancement_vs_transcendence =( 7+row['Self-Enhancement']-row['Self-Transcendence'])/2
        conservation = row['Conservation']
        tws = row['TWS']
        sociability = row['Sociability']
        valence = row['Valence']
        arousal = row['Arousal']
        energy = row['Energy']

        sbj = row['sbj']
        sex = row['sex']
        age = row['age']
        education = row['education']
        nationality = row['Nationality']
        ethnicity = row['Ethnicity']
        student_status = row['Student status']

        if student_status == 'No':
            student_status = 'Not a student'
        elif student_status == 'Yes':
            student_status = 'Currently a student'
        else:
            student_status = 'NA'

        country_of_residence = row['Country of residence']

        items_list = scene_settings[user_setting]
        random.shuffle(items_list)

        try:
            resp = task_generator.invoke({'messages': [
                    HumanMessage(content=generate_task_prompt.render(
                    scene=items_list, 
                    examples=examples,
                    num_tasks=n_tasks,
                    # individual difference
                    self_transcendence=self_transcendence,
                    self_enhancement=self_enhancement,
                    openness_to_change=openness_to_change,
                    conservation=conservation,
                    openness_vs_conservation=openness_vs_conservation,
                    enhancement_vs_transcendence=enhancement_vs_transcendence,
                    tws=tws,
                    sociability=sociability,
                    valence=valence,
                    arousal=arousal,
                    energy=ENERGY_DICT[energy],
                    # demographics
                    age=age,
                    sex=sex,
                    nationality=nationality,
                    ethnicity=ethnicity,
                    # No => currently {{ student_status }}
                    # Yes => currently {{ student_status }}
                    student_status=student_status,
                    education=education,
                    country_of_residence=country_of_residence,
                ))
            ]})
        
            # First get the structured output
            structure_resp = llm.with_structured_output(TasksReport).invoke(f'''Extract the task reports from the following text:
    {resp.content}
            ''')

            # Add validation step
            validation_prompt = """Please validate and correct the following task:
    Task description: {task_description}
    Current required items: {required_items}
    Available items in scene: {items_list}

    Please ensure:
    1. All required_items names must be identical to names from the available items list (must be character-for-character identical, including spaces and capitalization etc.)
    2. Do not use objects names outside of the provided available items list.
    3. If the task description mentions interaction with other people, include 'Other people' in required_items
    4. Each item should have a name and quantity

    Output the final required_items list in the following format, even if no corrections are needed:
    [{{"name": "item_name", "quantity": number}}, ...]"""

            # Validate each task
            # items_list => name
            items_list_name = [item[0] for item in items_list]

            for task in structure_resp.tasks:
                validation_resp = llm_mini.invoke(('human', validation_prompt.format(
                        task_description=task.task_description,
                        required_items=task.required_items,
                        items_list=items_list_name)
                ))
                correct_items = llm_mini.with_structured_output(RequiredItems).invoke(validation_resp.content)
                print('\noriginal:', task.required_items)
                print('correct:', correct_items.items)

                if 'Other people' not in items_list_name and 'Other people' in [item.name for item in correct_items.items]:
                    correct_items.items = [item for item in correct_items.items if item.name != 'Other people']
                    print('removed Other people', prolific_pid)

                task.required_items = correct_items.items

            print(f"Generated tasks: {len(structure_resp.tasks)}")
            for task in structure_resp.tasks:
                result_dict = {
                    'idx': idx,
                    'prolific_pid': prolific_pid,
                    'user_setting': user_setting,
                    'model_name': llm.model_name,
                    'temperature': llm.temperature,
                    'agent': 'naive', 
                    **task.dict(),
                    'raw_response': resp.content,
                }
                results.append(result_dict)
        except Exception as e:
            failed_pids.append(prolific_pid)
            print(f"Error for prolific_pid {prolific_pid}: {e}")

    print(f"Failed pids: {failed_pids}")
    df = pd.DataFrame(results)
    output_file = f'taskgen_traits_{llm.model_name}_{datetime.now().strftime("%m%d_%H%M")}.xlsx'
    df.to_excel(output_file, index=False)
    print(f"\nResults saved to {output_file}")
    return results

if __name__ == "__main__":

    assert load_dotenv(find_dotenv(filename=".env"))

    # os.environ['LANGCHAIN_PROJECT'] = f'task_gen_{datetime.now().strftime("%m%d_%H")}'

    model_id = "gpt-4o-2024-08-06"
    mini_id = "gpt-4o-mini-2024-07-18"
    
    region = 'eastus'

    llm = AzureChatOpenAI(
        model=model_id,
        temperature=1.0,
        api_version=os.getenv("AI_API_VERSION"),
        api_key=os.getenv("AI_OAI_API_KEY"),
        azure_endpoint=f'{os.getenv("AI_API_BASE")}/{region}',
    )

    llm_mini = AzureChatOpenAI(
        model=mini_id,
        temperature=1.0,
        api_version=os.getenv("AI_API_VERSION"),
        api_key=os.getenv("AI_OAI_API_KEY"),
        azure_endpoint=f'{os.getenv("AI_API_BASE")}/{region}',
    )

    task_generator = prepare_agent(llm)
    
    generate_task_prompt = Template(open("./prompts/roleplay/generate.txt").read())
    examples = open('./prompts/examples.txt').read()

    scene_settings = get_all_scene_settings_align()
    
    # one agent call: 15s
    gen_and_save_align_human_traits(scene_settings)
