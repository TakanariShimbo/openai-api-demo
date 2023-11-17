import streamlit as st

from handlers.image_recognition_handler import ImageRecognitionHandler
from handlers.image_handler import ImageHandler
from components.title_component import TitleComponent


TitleComponent.set_page_configs(
    icon="👀",
    title="Image Recognition",
)

with st.form(key="Image Recognition Form"):
    inputed_prompt = st.text_input(label="Prompt")
    uploaded_image = st.file_uploader(label="Uploader", type=["jpg", "jpeg", "png", "bmp"])
    is_submit = st.form_submit_button(label="Submit", type="primary")

if is_submit:
    if not inputed_prompt or not uploaded_image:
        st.warning("Please fill out the form completely...")
    else:
        with st.spinner(text="Image Loading..."):
            image_bytes = uploaded_image.getvalue()
            image_b64 = ImageHandler.bytes_to_b64(image_bytes=image_bytes)
            image_rgb = ImageHandler.bytes_to_array_rgb(image_bytes=image_bytes)
        st.image(image=image_rgb, caption=uploaded_image.name, use_column_width=True)
        
        answer_area = st.empty()
        ImageRecognitionHandler.query_and_display_answer_streamly(
            image_b64=image_b64,
            prompt=inputed_prompt,
            display_func=answer_area.write,
        )
