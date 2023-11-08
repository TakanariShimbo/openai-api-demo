from textwrap import dedent
import streamlit as st
from components.title_component import TitleComponent
from openai import OpenAI
from enums.env_enum import EnvEnum

"""
TITLE
"""
TitleComponent.set_page_configs(
    icon="🌅",
    title="Image Generator",
)


"""
CONTENTS
"""
def display_content() -> None:
    content = dedent(
        f"""
        このページでは画像生成を行います😊  
        by Ikezu Shun🍓
        """
    )
    st.markdown(content)

display_content()

client = OpenAI(api_key=EnvEnum.OPENAI_APIKEY.value)

text = st.text_input('生成したい画像のヒントを入力')
submit_button = st.button("送信", type="primary")

if submit_button:
  response = client.images.generate(
    model="dall-e-3",
    prompt=text,
    size="1024x1024",
    quality="standard",
    n=1,
  )
  
  image_url = response.data[0].url

  st.image(image_url, caption='生成された画像',use_column_width=True)
  st.markdown(f'[生成された画像(リンク)]({image_url})')
  st.balloons()