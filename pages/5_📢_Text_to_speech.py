import streamlit as st
from components.title_component import TitleComponent
from openai import OpenAI
import os
from enums.env_enum import EnvEnum

"""
TITLE
"""
TitleComponent.set_page_configs(
    icon="📢",
    title="Text to Speech",
)

def get_session_state(session_state_name: str):
    return st.session_state.get(session_state_name, None)

def set_session_state(session_state_name: str, value):
    st.session_state[session_state_name] = value

client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)

generation_form = st.form(key="Speech to text")
with generation_form:
    current_prompt = get_session_state("prompt")
    prompt = st.text_input(label="Prompt", value=current_prompt)
    generation_submit_button = st.form_submit_button(label="Sumbit", type="primary")

if generation_submit_button:
    set_session_state("prompt", prompt)
    with st.spinner("Generating"):
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=prompt
        )
        audio_bytes = bytes()
        for data in response.iter_bytes():
            audio_bytes += data
        set_session_state("audio_bytes", audio_bytes)

st.audio(data=get_session_state("audio_bytes"), format="audio/mp3")