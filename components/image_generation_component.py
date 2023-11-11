from typing import Union

import cv2
import numpy as np
import requests
import streamlit as st

from enums.image_generation_enum import (
    ImageGenerationModelEnum,
    ImageGenerationSizeEnum,
    ImageGenerationQualityEnum,
)
from session_states.image_generation_s_states import ImageGenerationSStates, ImageGenerationSStateDefaults
from handlers.enum_handler import EnumHandler
from handlers.image_generation_handler import ImageGenerationHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def on_submit_start():
        ImageGenerationSStates.set_submit_button_state(is_submitting=True)

    @staticmethod
    def on_submit_finish(inputed_user_prompt: str, generated_image: Union[np.ndarray, str]):
        ImageGenerationSStates.set_user_prompt(user_prompt=inputed_user_prompt)
        ImageGenerationSStates.set_generated_image(generated_image=generated_image)
        ImageGenerationSStates.set_submit_button_state()

    @staticmethod
    def generate_image(inputed_user_prompt: str) -> str:
        image_url = ImageGenerationHandler.get_image_url(
            prompt=inputed_user_prompt,
            model_type=ImageGenerationSStates.get_model_type(),
            size_type=ImageGenerationSStates.get_size_type(),
            quality_type=ImageGenerationSStates.get_quality_type(),
        )
        return image_url
    
    @staticmethod
    def convert_image(image_url: str) -> np.ndarray:
        response = requests.get(url=image_url)
        response.raise_for_status()
        image_bytes = bytearray(response.content)
        image_bgr = cv2.imdecode(buf=np.asarray(image_bytes, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(src=image_bgr, code=cv2.COLOR_BGR2RGB)
        return image_rgb


class ImageGenerationComponent:
    @classmethod
    def display_component(cls):
        res = cls.__sub_display_component()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

    @staticmethod
    def __sub_display_component() -> SubComponentResult:
        """
        SETTING
        """
        st.write("### Settings")
        setting_col = st.columns(3)
        # --- DALL-E Model select ---
        selected_model_value = setting_col[0].selectbox(
            label="DALL-E Model",
            options=EnumHandler.get_enum_member_values(enum=ImageGenerationModelEnum),
            index=EnumHandler.enum_member_to_index(member=ImageGenerationSStates.get_model_type()),
            placeholder="Select model...",
        )

        # --- Size select ---
        selected_size_value = setting_col[1].selectbox(
            label="Size",
            options=EnumHandler.get_enum_member_values(enum=ImageGenerationSizeEnum),
            index=EnumHandler.enum_member_to_index(member=ImageGenerationSStates.get_size_type()),
            placeholder="Select size...",
        )

        # --- Quality select ---
        selected_quality_value = setting_col[2].selectbox(
            label="Quality",
            options=EnumHandler.get_enum_member_values(enum=ImageGenerationQualityEnum),
            index=EnumHandler.enum_member_to_index(member=ImageGenerationSStates.get_quality_type()),
            placeholder="Quality size...",
        )

        if not selected_model_value or not selected_size_value or not selected_quality_value:
            st.error("Please select params...")
            return SubComponentResult(go_next=False)

        selected_model_type = EnumHandler.value_to_enum_member(enum=ImageGenerationModelEnum, value=selected_model_value)
        selected_size_type = EnumHandler.value_to_enum_member(enum=ImageGenerationSizeEnum, value=selected_size_value)
        selected_quality_type = EnumHandler.value_to_enum_member(enum=ImageGenerationQualityEnum, value=selected_quality_value)

        if ImageGenerationSStates.get_model_type() != selected_model_type:
            ImageGenerationSStates.set_model_type(model_type=selected_model_type)

        if ImageGenerationSStates.get_size_type() != selected_size_type:
            ImageGenerationSStates.set_size_type(size_type=selected_size_type)

        if ImageGenerationSStates.get_quality_type() != selected_size_type:
            ImageGenerationSStates.set_quality_type(quality_type=selected_quality_type)

        """
        Generation
        """
        st.write("### Generation")
        # --- Text area ---
        inputed_user_prompt = st.text_area(
            label="User Prompt",
            value=ImageGenerationSStates.get_user_prompt(),
            placeholder="Please enter a description of the image to be generated",
        )

        # --- Submit button ---
        is_submited = st.button(
            label="Sumbit",
            disabled=ImageGenerationSStates.get_submit_button_state(),
            on_click=OnSubmitHandler.on_submit_start,
            type="primary",
        )

        image_area = st.empty()
        if is_submited:
            image_area.image(image=ImageGenerationHandler.get_DUMMY_IMAGE(), caption="Loading...", use_column_width=True)
            generated_image_url = OnSubmitHandler.generate_image(inputed_user_prompt=inputed_user_prompt)
            generated_image_rgb = OnSubmitHandler.convert_image(image_url=generated_image_url)
            OnSubmitHandler.on_submit_finish(inputed_user_prompt=inputed_user_prompt, generated_image=generated_image_rgb)
            return SubComponentResult(call_rerun=True)
        
        generated_image = ImageGenerationSStates.get_generated_image()
        if type(generated_image) == type(None):
            return SubComponentResult()
        
        image_area.image(image=generated_image, caption=ImageGenerationSStates.get_user_prompt(), use_column_width=True)
        return SubComponentResult()
