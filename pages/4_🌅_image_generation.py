from textwrap import dedent
import streamlit as st
from components.title_component import TitleComponent

# from openai import OpenAI
# from enums.env_enum import EnvEnum

# from enums.sender_enum import SenderEnum
# from handlers.session_state_handler import SessionStateHandler
from enums.image_generator_enum import (
    ImageGeneratorModelEnum,
    ImageGeneratorSizeEnum,
    ImageGeneratorQualityEnum,
)
from handlers.image_generator_handler import ImageGeneratorHandler

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

# display model setting
with st.form("setting_form", clear_on_submit=True):
    st.write("### Settings")
    col = st.columns(3)
    selected_model_value = col[0].selectbox(
        label="DALL-E Model",
        options=ImageGeneratorModelEnum.to_value_list(),
        placeholder="Select model...",
    )
    st.session_state.model = selected_model_value
    selected_size_value = col[1].selectbox(
        label="Size",
        options=ImageGeneratorSizeEnum.to_value_list(),
        placeholder="Select size...",
    )
    selected_quality_value = col[2].selectbox(
        label="Quality",
        options=ImageGeneratorQualityEnum.to_value_list(),
        placeholder="Quality size...",
    )

    request_text = st.text_area(label="Description of the image", placeholder="Please enter a description of the image to be generated")
    submit_button = st.form_submit_button("Send", type="primary")

if not selected_model_value:
    st.error("Please select setting menu")

else:
    if submit_button:
        with st.spinner("Image generating..."):
            image_url = ImageGeneratorHandler.get_image_url(
                prompt=request_text,
                model=selected_model_value,
                size=selected_size_value,
                quality=selected_quality_value,
            )
            st.success("Generation complete!")
            st.image(image_url, caption=request_text, use_column_width=True)
            st.link_button("Image URL", image_url)
            st.balloons()
