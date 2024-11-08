import streamlit as st
import pandas as pd
import time
import os
import json
import shutil
from gpt4all import GPT4All


# Path to your local .gguf model file
project_path = os.path.dirname(os.path.abspath(__file__))
models_directory_path = os.path.join(project_path, "models") 
model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
model_path = os.path.join(models_directory_path, model_name)

os.makedirs(models_directory_path, exist_ok=True)

default_cache_path = os.path.expanduser("~/.cache/gpt4all/")
default_model_path = os.path.join(default_cache_path, model_name)


# Check if the model exists in the project folder
if not os.path.exists(model_path):
    # Download the model if not present in either location
    if not os.path.exists(default_model_path):
        print("Downloading the model to default cache...")
        model = GPT4All(model_name)  # Downloads to the default cache
    # Copy the model to the custom path if downloaded to cache
    if os.path.exists(default_model_path):
        print("Copying model to project models directory...")
        shutil.copy(default_model_path, model_path)
else:
    print("Model already exists in project folder, loading from disk...")

model = GPT4All(model_path, allow_download=False)

st.title("Activity Advisor")

json_structure = {
    "introduction": "",
    "conclusion": "",
    "activities": [
        {
            "title": "",
            "description": ""
        },
        {
            "title": "",
            "description": ""
        },
        {
            "title": "",
            "description": ""
        }
    ]    
}

activity_dict = {
    "Effektivitet": [
        "Använder resurser på bästa sätt",
        "Beslutsprocessen",
        "Gemensamt mål",
        "Planerar vårt arbete"
    ],
    "Delaktighet": [
        "Arbetssituation",
        "Kommentera på information",
        "Påverka beslut",
        "Påverka hur",
        "Påverka vad",
        "Tillräckligt med befogenheter"
    ],
    "Arbetsrelaterad utmattning": [
        "Känslomässigt tömd",
        "Trött",
        "Utsliten"
    ],
    "Medarbetarskap": [
        "Ansvar för kompetens",
        "Ansvar informerad",
        "Initiativ till förändring",
        "Öppen för förändring"
    ],
    "Återkoppling": [
        "Kommunicerat vad som förväntas",
        "Konstruktiv dialog",
        "Positiv feedback"
    ],
    "Medarbetarkraft": [
        "Irritation",
        "Koncentrationsvårigheter",
        "Oro",
        "Rastlöshet",
        "Uppgivenhet"
    ],
    "Lärande i arbetet": [
        "Arbete utveklande",
        "Kompetenser tas tillvara",
        "Utvecklas yrkesmässigt"
    ],
    "Arbetstakt": [
        "Fundera",
        "Genomföra",
        "Planera",
        "Reflektera"
    ],
    "Målkvalitet": [
        "Påverkningsbara",
        "Realistiska",
        "Tydliga",
        "Uppföljningsbara"
    ],
    "Ledarskap": [
        "Förklara hur vi ska nå målen",
        "Konsekvent agerande",
        "Tydlig kommunikation"
    ],
    "Socialt klimat": [
        "God sammanhållning",
        "Kollegor ställer upp",
        "Positiv stämning"
    ],
}

def get_prompt(index_area, index_question):
    text_prompt = f"""Skriv endast på svenska. Ge tre förslag på aktiviteter en avdelning kan göra för att förbättra:
        {index_area} om många av de anställda har svarat att följande kategori är ett problem: {index_question}.
        Lägg till en inledning och slutsats. Mata in all text i denna json string: {json_structure}
        Returnera endast json strängen UTAN en beskrivning, anteckning eller kommentar innan eller efter json strängen.
        """
    with model.chat_session():
        prompt = model.generate(text_prompt, max_tokens=4096)
    return prompt

def clean_json_string(json_string):
    # Remove trailing periods or other extraneous characters
    json_string = json_string.strip().rstrip('.')

    # Add a missing closing brace if possible
    if json_string.count('{') > json_string.count('}'):
        json_string += '}'
    elif json_string.count('[') > json_string.count(']'):
        json_string += ']'

    return json_string

def parse_json(json_string):
    json_string = clean_json_string(json_string)
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        print("JSON format issue, attempting to auto-correct.")
        # Additional handling or manual correction could go here if needed
        return None

def print_on_page(index_area, options):
    index_question = st.selectbox("Välj områdesfråga", list(options))
    get_prompt_button = st.button("Generera nya aktivitetsförslag!")

    directory_path = "promptfiles"
    file_path = f"{directory_path}/{index_area}_{index_question}.txt"

    os.makedirs(directory_path, exist_ok=True)

    if get_prompt_button:
        text = get_prompt(index_area, index_question)
        save_to_file(index_area, index_question, text)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            text = file.read()
            
    #st.write(text)
    json_object = parse_json(text)
    #st.write(json_object)
    introduction = json_object["introduction"]
    conclusion = json_object["conclusion"]
    activities = json_object["activities"]

    st.subheader("Aktivitets förslag:")
    st.write(introduction)
    activity_options = []
    for index, activity in enumerate(activities):
        activity_options.append(activity["title"])
        st.write(f"{index + 1}. **{activity["title"]}**: {activity["description"]}")
    st.write(conclusion)


    st.subheader("Välj en Aktivitet!")
    activity_selected = st.selectbox("Välj aktivitet", list(activity_options))

    start_activity_button = st.button("Start activity!")
    current_activity = activity_selected
    complete_activity_button = False
    if (start_activity_button):
        current_activity = activity_selected
        st.write(f"{current_activity} started!")
    
    complete_activity_button = st.button("Complete activity!")
       
    if (complete_activity_button):
        st.toast(f"{current_activity} was completed! A survey will be sent to your employees.")

def run_all_prompts(activity_dict):
    for index_area in activity_dict:
        st.write(f"{index_area} started!")
        for question in activity_dict[index_area]:

            text = get_prompt(index_area, question)
            save_to_file(index_area, question, text)

            time.sleep(0.1)
            st.write(f"- {question} is completed!")

def save_to_file(index_area, question, text):
    directory_path = "promptfiles"
    file_path = f"{directory_path}/{index_area}_{question}.txt"
    os.makedirs(directory_path, exist_ok=True)

    # Find the first occurrence of '{' and the last occurrence of '}'
    start = text.find('{')
    end = text.rfind('}')

    # Extract the substring
    if start != -1 and end != -1:
        extracted_text = text[start:end + 1]
    else:
        extracted_text = "Couldn't find a json format in the string."

    with open(file_path, 'w') as file:
        file.write(extracted_text)


run_all_prompts_button = st.button("Run all prompts")
if (run_all_prompts_button):
    run_all_prompts(activity_dict)
