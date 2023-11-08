import base64
import streamlit as st
import numpy as np
import os
import cv2

from openai import OpenAI
from PIL import Image
from enums.env_enum import EnvEnum
from components.title_component import TitleComponent

client = OpenAI(api_key=EnvEnum.OPENAI_APIKEY.value)

TitleComponent.set_page_configs(
    icon="👀",
    title="Image Recognition",
)

def encode_image(image_array):
    _, img_encoded = cv2.imencode('.jpeg', image_array)
    img_b64 = base64.b64encode(img_encoded).decode('utf-8') 
    return img_b64         

upload_image=st.file_uploader("ファイルアップロード", type='jpeg')
if upload_image is not None:
    image=Image.open(upload_image)
    img_array = np.array(image)
    st.image(img_array,caption = 'アップロード画像',use_column_width = True)

    base64_image = encode_image(img_array)

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "これは何の画像ですか？"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    st.write(response.choices[0].message.content)