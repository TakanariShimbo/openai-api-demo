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
from session_states.image_generation_s_states import ImageGenerationSStates
from handlers.enum_handler import EnumHandler
from handlers.image_generation_handler import ImageGenerationHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def lock_submit_button() -> None:
        ImageGenerationSStates.set_submit_button_state(is_submitting=True)

    @staticmethod
    def unlock_submit_button() -> None:
        ImageGenerationSStates.set_submit_button_state()

    @staticmethod
    def generate_image(
        inputed_prompt: str,
        selected_model_type: ImageGenerationModelEnum,
        selected_size_type: ImageGenerationSizeEnum,
        selected_quality_type: ImageGenerationQualityEnum,
    ) -> str:
        image_url = ImageGenerationHandler.get_image_url(
            prompt=inputed_prompt,
            model_type=selected_model_type,
            size_type=selected_size_type,
            quality_type=selected_quality_type,
        )
        return image_url

    @staticmethod
    def download_image(image_url: str) -> np.ndarray:
        response = requests.get(url=image_url)
        response.raise_for_status()
        image_bytes = bytearray(response.content)
        image_bgr = cv2.imdecode(buf=np.asarray(image_bytes, dtype=np.uint8), flags=cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(src=image_bgr, code=cv2.COLOR_BGR2RGB)
        return image_rgb

    @staticmethod
    def update_s_states(
        selected_model_type: ImageGenerationModelEnum,
        selected_size_type: ImageGenerationSizeEnum,
        selected_quality_type: ImageGenerationQualityEnum,
        inputed_prompt: str,
        generated_image: Union[np.ndarray, str],
    ) -> None:
        ImageGenerationSStates.set_model_type(model_type=selected_model_type)
        ImageGenerationSStates.set_size_type(size_type=selected_size_type)
        ImageGenerationSStates.set_quality_type(quality_type=selected_quality_type)
        ImageGenerationSStates.set_inputed_prompt(inputed_prompt=inputed_prompt)
        ImageGenerationSStates.set_generated_image(generated_image=generated_image)


class ImageGenerationComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        form = st.form(key="Image Generation Form")
        with form:
            setting_col = st.columns(3)

            # --- DALL-E Model select ---
            selected_model_value = setting_col[0].selectbox(
                label="Model",
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

            # --- Text area ---
            inputed_prompt = st.text_area(
                label="Prompt",
                value=ImageGenerationSStates.get_inputed_prompt(),
                placeholder="Please enter a description of the image to be generated",
            )

            # --- Submit button ---
            is_submited = st.form_submit_button(
                label="Sumbit",
                disabled=ImageGenerationSStates.get_submit_button_state(),
                on_click=OnSubmitHandler.lock_submit_button,
                type="primary",
            )

        if is_submited:
            if not selected_model_value or not selected_size_value or not selected_quality_value or not inputed_prompt:
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)

            selected_model_type = EnumHandler.value_to_enum_member(enum=ImageGenerationModelEnum, value=selected_model_value)
            selected_size_type = EnumHandler.value_to_enum_member(enum=ImageGenerationSizeEnum, value=selected_size_value)
            selected_quality_type = EnumHandler.value_to_enum_member(enum=ImageGenerationQualityEnum, value=selected_quality_value)

            with st.status("Generating..."):
                st.write("Querying...")
                generated_image_url = OnSubmitHandler.generate_image(
                    inputed_prompt=inputed_prompt,
                    selected_model_type=selected_model_type,
                    selected_size_type=selected_size_type,
                    selected_quality_type=selected_quality_type,
                )
                st.write("Downloading...")
                generated_image_rgb = OnSubmitHandler.download_image(image_url=generated_image_url)

            OnSubmitHandler.update_s_states(
                selected_model_type=selected_model_type,
                selected_size_type=selected_size_type,
                selected_quality_type=selected_quality_type,
                inputed_prompt=inputed_prompt,
                generated_image=generated_image_rgb,
            )
            
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        if not selected_model_value or not selected_size_value or not selected_quality_value or not inputed_prompt:
            with form:
                st.warning("Please fill out the form completely.")
        
        st.image(
            image=ImageGenerationSStates.get_generated_image(),
            caption=ImageGenerationSStates.get_inputed_prompt(),
            use_column_width=True,
        )
        return SubComponentResult()
