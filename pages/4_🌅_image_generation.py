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


def get_index(model_list: list, label: str) -> Optional[int]:
    if not label:
        return None
    return model_list.index(label)

    # display model setting

st.write("### Settings")
col = st.columns(3)
current_model_label = SessionStateHandler.get_image_generation_model_label()
selected_model_label = col[0].selectbox(
    label="DALL-E Model",
    options=ImageGenerationModelEnum.to_value_list(),
    index=get_index(ImageGenerationModelEnum.to_value_list(), current_model_label),
    placeholder="Select model...",
)
if selected_model_label:
    SessionStateHandler.set_image_generation_model_label(model_label=selected_model_label)

selected_size_label = col[1].selectbox(
    label="Size",
    options=ImageGenerationSizeEnum.to_value_list(),
    placeholder="Select size...",
)
selected_quality_label = col[2].selectbox(
    label="Quality",
    options=ImageGenerationQualityEnum.to_value_list(),
    placeholder="Quality size...",
)

request_text = st.text_area(
    label="Description of the image",
    placeholder="Please enter a description of the image to be generated",
)
submit_button = st.button("Send", type="primary")


if not selected_model_label:
    st.error("Please select setting menu")

else:
    if submit_button:
        with st.spinner("Image generating..."):
            image_url = ImageGenerationHandler.get_image_url(
                prompt=request_text,
                model=selected_model_label,
                size=selected_size_label,
                quality=selected_quality_label,
            )
            st.success("Generation complete!")
            st.image(image_url, caption=request_text, use_column_width=True)
            st.link_button("Image URL", image_url)
            st.balloons()
