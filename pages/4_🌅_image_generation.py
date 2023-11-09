from textwrap import dedent
import streamlit as st
from components.title_component import TitleComponent

# from openai import OpenAI
# from enums.env_enum import EnvEnum

# from enums.sender_enum import SenderEnum
from handlers.session_state_handler import SessionStateHandler
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
    image_url = SessionStateHandler.get_image_generation_image_url()
    if not image_url:
        return
    
    st.image(image_url, caption=request_text, use_column_width=True)
    st.link_button("Image URL", image_url)

    # display model setting

st.write("### Settings")
setting_col = st.columns(3)
# --- DALL-E Model select ---
current_model_label = SessionStateHandler.get_image_generation_model_label()
selected_model_label = setting_col[0].selectbox(
    label="DALL-E Model",
    options=ImageGenerationModelEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationModelEnum.to_value_list(), current_label=current_model_label, default_label=ImageGenerationModelEnum.DALL_E_3.value),
    placeholder="Select model...",
)
if selected_model_label:
    SessionStateHandler.set_image_generation_model_label(model_label=selected_model_label)

# --- Size select ---
current_size_label = SessionStateHandler.get_image_generation_size_label()
selected_size_label = setting_col[1].selectbox(
    label="Size",
    options=ImageGenerationSizeEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationSizeEnum.to_value_list(), current_label=current_size_label, default_label=ImageGenerationSizeEnum.SIZE_1024X1024.value),
    placeholder="Select size...",
)
if selected_size_label:
    SessionStateHandler.set_image_generation_size_label(size_label=selected_size_label)

# --- Quality select ---
current_quality_label = SessionStateHandler.get_image_generation_quality_label()
selected_quality_label = setting_col[2].selectbox(
    label="Quality",
    options=ImageGenerationQualityEnum.to_value_list(),
    index=ImageGenerationHandler.select_and_get_label(input_list=ImageGenerationQualityEnum.to_value_list(), current_label=current_quality_label, default_label=ImageGenerationQualityEnum.STANDARD.value),
    placeholder="Quality size...",
)
if selected_quality_label:
    SessionStateHandler.set_image_generation_quality_label(quality_label=selected_quality_label)

# --- Text area ---
current_description = SessionStateHandler.get_image_generation_description()
request_text = st.text_area(
    label="Description of the image",
    value=current_description,
    placeholder="Please enter a description of the image to be generated",
)
if request_text:
    SessionStateHandler.set_image_generation_description(description=request_text)

submit_button = st.button("Send", type="primary")


if not (selected_model_label or selected_quality_label or selected_quality_label):
    st.error("Please select setting menu")

else:
    if submit_button:
        with st.spinner("Image generating..."):
            current_image_url = SessionStateHandler.get_image_generation_image_url()
            image_url = ImageGenerationHandler.get_image_url(
                prompt=request_text,
                model=selected_model_label,
                size=selected_size_label,
                quality=selected_quality_label,
            )
            if image_url:
                SessionStateHandler.set_image_generation_image_url(image_url=image_url)
            st.success("Generation complete!")
            st.balloons()

    display_image()


