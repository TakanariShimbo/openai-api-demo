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
        Powered by DALL·E 3
        Made by Shun🍓
        """
    )
    st.markdown(content)

display_content()

client = OpenAI(api_key=EnvEnum.OPENAI_APIKEY.value)

request_text = st.text_input('生成したい画像のヒントを入力')
submit_button = st.button("送信", type="primary")

if submit_button:
  with st.spinner('画像生成中…'):
    response = client.images.generate(
      model="dall-e-3",
      prompt=request_text,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    st.success('生成完了！')
  
  image_url = response.data[0].url

  st.image(image_url, caption=request_text, use_column_width=True)

  st.link_button("画像(リンク)", image_url)
  st.balloons()