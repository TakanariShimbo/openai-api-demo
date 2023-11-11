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


upload_image = st.file_uploader(label="Upload Image", type=["jpg", "jpeg", "png", "bmp"])
if upload_image is not None:
    with st.spinner(text="Loading..."):
        image_bytes = upload_image.getvalue()
        image_b64 = base64.b64encode(s=image_bytes).decode()
        image_bgr = cv2.imdecode(
            buf=np.frombuffer(buffer=image_bytes, dtype=np.uint8),
            flags=cv2.IMREAD_COLOR,
        )
        image_rgb = cv2.cvtColor(src=image_bgr, code=cv2.COLOR_BGR2RGB)

    st.image(image=image_rgb, caption=upload_image.name, use_column_width=True)

    answer_area = st.empty()
    ImageRecognitionHandler.query_and_display_answer_streamly(
        image_b64=image_b64,
        display_func=answer_area.write,
    )
