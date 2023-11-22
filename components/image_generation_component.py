from typing import Union

import numpy as np
from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.image_generation_enum import AiModelEnum, SizeEnum, QualityEnum
from handlers.enum_handler import EnumHandler
from handlers.image_handler import ImageHandler
from handlers.image_generation_handler import ImageGenerationHandler
from s_states.image_generation_s_states import SubmitSState, ErrorMessageSState, AiModelTypeSState, SizeTypeSState, QualityTypeSState, StoredPromptSState, StoredImageSState
from components.sub_compornent_result import SubComponentResult


class FormSchema(BaseModel):
    ai_model_type: AiModelEnum
    size_type: SizeEnum
    quality_type: QualityEnum
    prompt: str = Field(min_length=1)


class OnSubmitHandler:
    @staticmethod
    def lock_submit_button():
        SubmitSState.set(value=True)

    @staticmethod
    def unlock_submit_button():
        SubmitSState.reset()

    @staticmethod
    def set_error_message(error_message: str = "Please fill out the form completely.") -> None:
        ErrorMessageSState.set(value=error_message)

    @staticmethod
    def reset_error_message() -> None:
        ErrorMessageSState.reset()

    @staticmethod
    def generate_image(form_schema: FormSchema) -> str:
        image_url = ImageGenerationHandler.generate_image(
            prompt=form_schema.prompt,
            model_type=form_schema.ai_model_type,
            size_type=form_schema.size_type,
            quality_type=form_schema.quality_type,
        )
        return image_url

    @staticmethod
    def download_image(image_url: str) -> np.ndarray:
        return ImageHandler.download_as_array_rgb(image_url=image_url)

    @staticmethod
    def update_s_states(
        form_schema: FormSchema,
        generated_image: Union[np.ndarray, str],
    ) -> None:
        AiModelTypeSState.set(value=form_schema.ai_model_type)
        SizeTypeSState.set(value=form_schema.size_type)
        QualityTypeSState.set(value=form_schema.quality_type)
        StoredPromptSState.set(value=form_schema.prompt)
        StoredImageSState.set(value=generated_image)


class ImageGenerationComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        form_dict = {}
        form = st.form(key="ImageGeneration_Form", clear_on_submit=True)
        with form:
            st.markdown("#### Form")
            left_col, center_col, right_col = st.columns(3)

            form_dict["ai_model_type"] = left_col.selectbox(
                label="Model",
                options=EnumHandler.get_enum_members(enum=AiModelEnum),
                format_func=lambda x: x.name,
                index=EnumHandler.enum_member_to_index(member=AiModelTypeSState.get()),
                placeholder="Select model...",
                key="ImageGeneration_ModelSelectBox",
            )

            form_dict["size_type"] = center_col.selectbox(
                label="Size",
                options=EnumHandler.get_enum_members(enum=SizeEnum),
                format_func=lambda x: x.name,
                index=EnumHandler.enum_member_to_index(member=SizeTypeSState.get()),
                placeholder="Select size...",
                key="ImageGeneration_SizeSelectBox",
            )

            form_dict["quality_type"] = right_col.selectbox(
                label="Quality",
                options=EnumHandler.get_enum_members(enum=QualityEnum),
                format_func=lambda x: x.name,
                index=EnumHandler.enum_member_to_index(member=QualityTypeSState.get()),
                placeholder="Quality size...",
                key="ImageGeneration_QualitySelectBox",
            )

            form_dict["prompt"] = st.text_area(
                label="Prompt",
                disabled=SubmitSState.get(),
                placeholder="Please input prompt...",
                key="ImageGeneration_PromptTextArea",
            )

            is_submited = st.form_submit_button(
                label="Submit",
                disabled=SubmitSState.get(),
                on_click=OnSubmitHandler.lock_submit_button,
                type="primary",
            )

        if is_submited:
            try:
                form_schema = FormSchema(**form_dict)
            except ValidationError:
                OnSubmitHandler.set_error_message()
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)

            with form:
                with st.status("Generating..."):
                    st.write("Querying...")
                    generated_image_url = OnSubmitHandler.generate_image(form_schema=form_schema)
                    st.write(f"[Downloading...]({generated_image_url})")
                    generated_image_rgb = OnSubmitHandler.download_image(image_url=generated_image_url)

            OnSubmitHandler.update_s_states(
                form_schema=form_schema,
                generated_image=generated_image_rgb,
            )

            OnSubmitHandler.reset_error_message()
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        try:
            form_schema = FormSchema(**form_dict)
        except ValidationError:
            error_message = ErrorMessageSState.get()
            if error_message:
                with form:
                    st.warning(error_message)

        st.markdown("#### Result")
        st.image(
            image=StoredImageSState.get(),
            caption=StoredPromptSState.get(),
            use_column_width=True,
        )
        return SubComponentResult()
