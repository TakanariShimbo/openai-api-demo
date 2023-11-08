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
        このページでは画像生成を行います😊  
        Powered by DALL·E  
        Made by Shun🍓  
        """
    )
    st.markdown(content)


display_content()

# display model setting
st.write("### Model Setting")
selected_model_value = st.selectbox(
    label="DALL-E Model",
    options=ImageGeneratorModelEnum.to_value_list(),
    placeholder="Select model...",
)

st.write("### Size Setting")
selected_size_value = st.selectbox(
    label="Size",
    options=ImageGeneratorSizeEnum.to_value_list(),
    placeholder="Select size...",
)

st.write("### Quality Setting")
selected_quality_value = st.selectbox(
    label="Size",
    options=ImageGeneratorQualityEnum.to_value_list(),
    placeholder="Quality size...",
)

request_text = st.text_input("生成したい画像のヒントを入力")
submit_button = st.button("送信", type="primary")

if not selected_model_value:
    st.error("Please select model...")

else:
    if submit_button:
        with st.spinner("画像生成中…"):
            image_url = ImageGeneratorHandler.get_image_url(
                prompt=request_text,
                model=selected_model_value,
                size=selected_size_value,
                quality=selected_quality_value,
            )
            st.image(image_url, caption=request_text, use_column_width=True)
            st.link_button("画像リンク", image_url)
            st.success("生成完了！")
            st.balloons()
