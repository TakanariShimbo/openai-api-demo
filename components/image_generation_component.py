from typing import Union

import numpy as np
from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.image_generation_enum import ModelEnum, SizeEnum, QualityEnum
from session_states.image_generation_s_states import SubmitSState, ErrorMessageSState, ModelSState, SizeSState, QualitySState, PromptSState, GeneratedImageSState
from handlers.enum_handler import EnumHandler
from handlers.image_handler import ImageHandler
from handlers.image_generation_handler import ImageGenerationHandler
from components.base import SubComponentResult


class FormSchema(BaseModel):
    model: str
    size: str
    quality: str
    prompt: str = Field(min_length=1)

    @property
    def model_type(self) -> ModelEnum:
        return EnumHandler.value_to_enum_member(enum=ModelEnum, value=self.model)

    @property
    def size_type(self) -> SizeEnum:
        return EnumHandler.value_to_enum_member(enum=SizeEnum, value=self.size)

    @property
    def quality_type(self) -> QualityEnum:
        return EnumHandler.value_to_enum_member(enum=QualityEnum, value=self.quality)


class OnSubmitHandler:
    @staticmethod
    def lock_submit_button():
        SubmitSState.set(value=True)

    @staticmethod
    def unlock_submit_button():
        SubmitSState.reset()

    @staticmethod
    def generate_image(form_schema: FormSchema) -> str:
        image_url = ImageGenerationHandler.get_image_url(
            prompt=form_schema.prompt,
            model_type=form_schema.model_type,
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
        ModelSState.set(value=form_schema.model_type)
        SizeSState.set(value=form_schema.size_type)
        QualitySState.set(value=form_schema.quality_type)
        PromptSState.set(value=form_schema.prompt)
        GeneratedImageSState.set(value=generated_image)

    @staticmethod
    def set_error_message(error_message: str = "Please fill out the form completely.") -> None:
        ErrorMessageSState.set(value=error_message)

    @staticmethod
    def reset_error_message() -> None:
        ErrorMessageSState.reset()


class ImageGenerationComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        form_dict = {}
        form = st.form(key="Image Generation Form")
        with form:
            left_col, center_col, right_col = st.columns(3)

            form_dict["model"] = left_col.selectbox(
                label="Model",
                options=EnumHandler.get_enum_member_values(enum=ModelEnum),
                index=EnumHandler.enum_member_to_index(member=ModelSState.get()),
                placeholder="Select model...",
                key="DallE ModelSelectBox",
            )

            form_dict["size"] = center_col.selectbox(
                label="Size",
                options=EnumHandler.get_enum_member_values(enum=SizeEnum),
                index=EnumHandler.enum_member_to_index(member=SizeSState.get()),
                placeholder="Select size...",
                key="DallE SizeSelectBox",
            )

            form_dict["quality"] = right_col.selectbox(
                label="Quality",
                options=EnumHandler.get_enum_member_values(enum=QualityEnum),
                index=EnumHandler.enum_member_to_index(member=QualitySState.get()),
                placeholder="Quality size...",
                key="DallE QualitySelectBox",
            )

            form_dict["prompt"] = st.text_area(
                label="Prompt",
                disabled=SubmitSState.get(),
                value=PromptSState.get(),
                placeholder="Please enter a description of the image to be generated",
                key="DallE PromptTextArea",
            )

            is_submited = st.form_submit_button(
                label="Sumbit",
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

        st.image(
            image=GeneratedImageSState.get(),
            caption=PromptSState.get(),
            use_column_width=True,
        )
        return SubComponentResult()
