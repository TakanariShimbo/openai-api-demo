from textwrap import dedent
import streamlit as st
from components.title_component import TitleComponent

# from openai import OpenAI
# from enums.env_enum import EnvEnum

# from enums.sender_enum import SenderEnum
from session_states.image_generation_session_states import ImageGenerationSessionStates
from enums.image_generation_enum import (
    ImageGenerationModelEnum,
    ImageGenerationSizeEnum,
    ImageGenerationQualityEnum,
)
from handlers.image_generation_handler import ImageGenerationHandler

from typing import Optional

"""
TITLE
"""
TitleComponent.set_page_configs(
    icon="🌅",
    title="Image Generation",
)


"""
CONTENTS
"""


def display_content() -> None:
    content = dedent(
        f"""
        This page performs image generation powered by DALL-E😊  
        Made by Shun🍓  
        """
    )
    st.markdown(content)


display_content()

def display_image():
    image_url = ImageGenerationSessionStates.get_image_url()
    if not image_url:
        return
    
    st.image(image_url, caption=request_text, use_column_width=True)
    st.link_button("Image URL", image_url)

    # display model setting

st.write("### Settings")
setting_col = st.columns(3)
# --- DALL-E Model select ---
current_model_label = ImageGenerationSessionStates.get_model_index()
selected_model_label = setting_col[0].selectbox(
    label="DALL-E Model",
    options=ImageGenerationModelEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationModelEnum.to_value_list(), current_label=current_model_label, default_label=ImageGenerationModelEnum.DALL_E_3.value),
    placeholder="Select model...",
)
if selected_model_label:
    ImageGenerationSessionStates.set_model_index(model_label=selected_model_label)

# --- Size select ---
current_size_label = ImageGenerationSessionStates.get_size_index()
selected_size_label = setting_col[1].selectbox(
    label="Size",
    options=ImageGenerationSizeEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationSizeEnum.to_value_list(), current_label=current_size_label, default_label=ImageGenerationSizeEnum.SIZE_1024X1024.value),
    placeholder="Select size...",
)
if selected_size_label:
    ImageGenerationSessionStates.set_size_index(size_label=selected_size_label)

# --- Quality select ---
current_quality_label = ImageGenerationSessionStates.get_quality_index()
selected_quality_label = setting_col[2].selectbox(
    label="Quality",
    options=ImageGenerationQualityEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationQualityEnum.to_value_list(), current_label=current_quality_label, default_label=ImageGenerationQualityEnum.STANDARD.value),
    placeholder="Quality size...",
)
if selected_quality_label:
    ImageGenerationSessionStates.set_quality_index(quality_label=selected_quality_label)

# --- Text area ---
current_description = ImageGenerationSessionStates.get_user_prompt()
request_text = st.text_area(
    label="Description of the image",
    value=current_description,
    placeholder="Please enter a description of the image to be generated",
)
if request_text:
    ImageGenerationSessionStates.set_user_prompt(user_prompt=request_text)

submit_button = st.button("Send", type="primary")


if not (selected_model_label or selected_quality_label or selected_quality_label):
    st.error("Please select setting menu")

else:
    if submit_button:
        with st.spinner("Image generating..."):
            current_image_url = ImageGenerationSessionStates.get_image_url()
            image_url = ImageGenerationHandler.get_image_url(
                prompt=request_text,
                model=selected_model_label,
                size=selected_size_label,
                quality=selected_quality_label,
            )
            if image_url:
                ImageGenerationSessionStates.set_image_url(image_url=image_url)
            st.success("Generation complete!")
            st.balloons()

    display_image()


