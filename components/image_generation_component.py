import streamlit as st

from enums.image_generation_enum import (
    ImageGenerationModelEnum,
    ImageGenerationSizeEnum,
    ImageGenerationQualityEnum,
)
from session_states.image_generation_s_states import ImageGenerationSStates
from handlers.image_generation_handler import ImageGenerationHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def on_submit_start():
        ImageGenerationSStates.set_submit_button_state(is_submitting=True)

    @staticmethod
    def on_submit_finish():
        ImageGenerationSStates.set_submit_button_state(is_submitting=False)

    @staticmethod
    def generate_image() -> None:
        with st.spinner("Image generating..."):
            image_url = ImageGenerationHandler.get_image_url(
                prompt=ImageGenerationSStates.get_user_prompt(),
                model_type=ImageGenerationSStates.get_model_type(),
                size_type=ImageGenerationSStates.get_size_type(),
                quality_type=ImageGenerationSStates.get_quality_type(),
            )
        ImageGenerationSStates.set_image_url(image_url=image_url)


class ImageGenerationComponent:
    @classmethod
    def display_component(cls):
        res = cls.__step1_apply_setting()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = cls.__step2_generate_image()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return
        
        res = cls.__step3_display_image()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return
        
    @staticmethod
    def __step1_apply_setting() -> SubComponentResult:
        st.write("### Settings")
        setting_col = st.columns(3)
        # --- DALL-E Model select ---
        selected_model_value = setting_col[0].selectbox(
            label="DALL-E Model",
            options=ImageGenerationModelEnum.to_value_list(),
            index=ImageGenerationModelEnum.from_type_to_index(enum=ImageGenerationSStates.get_model_type()),
            placeholder="Select model...",
        )

        # --- Size select ---
        selected_size_value = setting_col[1].selectbox(
            label="Size",
            options=ImageGenerationSizeEnum.to_value_list(),
            index=ImageGenerationSizeEnum.from_type_to_index(enum=ImageGenerationSStates.get_size_type()),
            placeholder="Select size...",
        )

        # --- Quality select ---
        selected_quality_value = setting_col[2].selectbox(
            label="Quality",
            options=ImageGenerationQualityEnum.to_value_list(),
            index=ImageGenerationQualityEnum.from_type_to_index(enum=ImageGenerationSStates.get_quality_type()),
            placeholder="Quality size...",
        )

        # --- Text area ---
        inputed_user_prompt = st.text_area(
            label="User Prompt",
            value=ImageGenerationSStates.get_user_prompt(),
            placeholder="Please enter a description of the image to be generated",
        )
        
        if not selected_model_value or not selected_size_value or not selected_quality_value:
            st.error("Please select params...")
            return SubComponentResult(go_next=False)
        
        selected_model_type = ImageGenerationModelEnum.from_value_to_type(value=selected_model_value)
        selected_size_type = ImageGenerationSizeEnum.from_value_to_type(value=selected_size_value)
        selected_quality_type = ImageGenerationQualityEnum.from_value_to_type(value=selected_quality_value)

        if ImageGenerationSStates.get_model_type() != selected_model_type:
            ImageGenerationSStates.set_model_type(model_type=selected_model_type)

        if ImageGenerationSStates.get_size_type() != selected_size_type:
            ImageGenerationSStates.set_size_type(size_type=selected_size_type)

        if ImageGenerationSStates.get_quality_type() != selected_size_type:
            ImageGenerationSStates.set_quality_type(quality_type=selected_quality_type)

        if inputed_user_prompt:
            ImageGenerationSStates.set_user_prompt(user_prompt=inputed_user_prompt)

        return SubComponentResult()

    @staticmethod
    def __step2_generate_image() -> SubComponentResult:
        # --- Submit button ---
        is_submited = st.button("Send", disabled=ImageGenerationSStates.get_submit_button_state(), on_click=OnSubmitHandler.on_submit_start, type="primary")
        if not is_submited:
            return SubComponentResult()
        
        OnSubmitHandler.generate_image()
        OnSubmitHandler.on_submit_finish()
        return SubComponentResult(call_rerun=True)


    @staticmethod
    def __step3_display_image() -> SubComponentResult:
        image_url = ImageGenerationSStates.get_image_url()
        if not image_url:
            return SubComponentResult()

        st.write("### Generated Image")
        st.image(image_url, caption=ImageGenerationSStates.get_user_prompt(), use_column_width=True)
        st.link_button("Image URL", image_url)
        return SubComponentResult()