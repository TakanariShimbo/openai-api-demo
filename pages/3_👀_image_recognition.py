import base64

import cv2
import numpy as np
import streamlit as st

from handlers.image_recognition_handler import ImageRecognitionHandler
from components.title_component import TitleComponent


TitleComponent.set_page_configs(
    icon="👀",
    title="Image Recognition",
)

with st.form(key="Image Recognition Form"):
    inputed_prompt = st.text_input(label="Prompt")
    uploaded_image = st.file_uploader(label="Uploader", type=["jpg", "jpeg", "png", "bmp"])
    is_submit = st.form_submit_button(label="Submit")

if is_submit:
    if not inputed_prompt or not uploaded_image:
        st.warning("Please fill out the form completely...")
    else:
        with st.spinner(text="Image Loading..."):
            image_bytes = uploaded_image.getvalue()
            image_b64 = base64.b64encode(s=image_bytes).decode()
            image_bgr = cv2.imdecode(
                buf=np.frombuffer(buffer=image_bytes, dtype=np.uint8),
                flags=cv2.IMREAD_COLOR,
            )
            image_rgb = cv2.cvtColor(src=image_bgr, code=cv2.COLOR_BGR2RGB)

        st.image(image=image_rgb, caption=uploaded_image.name, use_column_width=True)
        
        answer_area = st.empty()
        ImageRecognitionHandler.query_and_display_answer_streamly(
            image_b64=image_b64,
            prompt=inputed_prompt,
            display_func=answer_area.write,
        )
