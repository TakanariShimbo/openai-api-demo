import streamlit as st

from handlers.speech_generation_handler import SpeechGenerationHandler
from components.title_component import TitleComponent


"""
TITLE
"""
TitleComponent.set_page_configs(
    icon="📢",
    title="Text to Speech",
)

form = st.form(key="Speech to text form")
with form:
    inputed_prompt = st.text_input(label="Prompt", placeholder="Please enter a description of the speech to be generated")
    generation_submit_button = st.form_submit_button(label="Sumbit", type="primary")

if generation_submit_button:
    if not inputed_prompt:
        st.warning("Please fill out the form completely...")
    else:
        with st.spinner("Generating"):
            speech_bytes = SpeechGenerationHandler.get_speech_bytes(
                prompt=inputed_prompt,
            )

        st.audio(data=speech_bytes, format="audio/mp3")