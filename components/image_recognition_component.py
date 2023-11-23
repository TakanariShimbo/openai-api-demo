from typing import Optional

import numpy as np
from openai import OpenAI, AuthenticationError
from pydantic import BaseModel, ValidationError, Field
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from enums.image_recognition_enum import ExtensionEnum
from handlers.image_handler import ImageHandler
from handlers.enum_handler import EnumHandler
from handlers.image_recognition_handler import ImageRecognitionHandler
from s_states.image_recognition_s_states import SubmitSState, ErrorMessageSState, StoredPromptSState, StoredImageSState, StoredAnswerSState
from components.sub_compornent_result import SubComponentResult


class FormSchema(BaseModel):
    prompt: str = Field(min_length=1)
    image_bytes: bytes

    @classmethod
    def construct_using_form_dict(cls, prompt: str, uploaded_image: UploadedFile):
        return cls(prompt=prompt, image_bytes=uploaded_image.getvalue())

    @property
    def image_b64(self) -> str:
        return ImageHandler.bytes_to_b64(image_bytes=self.image_bytes)

    @property
    def image_array_rgb(self) -> np.ndarray:
        return ImageHandler.bytes_to_array_rgb(image_bytes=self.image_bytes)


class OnSubmitHandler:
    @staticmethod
    def lock_submit_button():
        SubmitSState.set(value=True)

    @staticmethod
    def unlock_submit_button():
        SubmitSState.reset()

    @staticmethod
    def set_error_message(error_message: str) -> None:
        ErrorMessageSState.set(value=error_message)

    @staticmethod
    def reset_error_message() -> None:
        ErrorMessageSState.reset()

    @staticmethod
    def display_uploaded_image(form_schema: FormSchema) -> None:
        st.image(
            image=form_schema.image_array_rgb,
            caption=form_schema.prompt,
            use_column_width=True,
        )

    @staticmethod
    def query_answer_and_display_streamly(client: OpenAI, form_schema: FormSchema) -> Optional[str]:
        answer_area = st.empty()
        answer = ImageRecognitionHandler.query_answer_and_display_streamly(
            client=client,
            image_b64=form_schema.image_b64,
            prompt=form_schema.prompt,
            display_func=answer_area.write,
        )
        return answer

    @staticmethod
    def update_s_states(form_schema: FormSchema, answer: Optional[str]):
        StoredPromptSState.set(value=form_schema.prompt)
        StoredImageSState.set(value=form_schema.image_array_rgb)
        if answer:
            StoredAnswerSState.set(value=answer)


class ImageRecognitionComponent:
    @classmethod
    def display_component(cls, client: OpenAI) -> None:
        res = cls.__sub_component(client=client)
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component(client: OpenAI) -> SubComponentResult:
        form_dict = {}
        form = st.form(key="ImageRecognition_Form", clear_on_submit=True)
        with form:
            st.markdown("#### Form")

            form_dict["prompt"] = st.text_input(
                label="Prompt",
                disabled=SubmitSState.get(),
                placeholder="Please input prompt...",
                key="ImageRecognition_PromptInput",
            )

            form_dict["uploaded_image"] = st.file_uploader(
                label="Uploader",
                type=EnumHandler.get_enum_member_values(enum=ExtensionEnum),
                key="ImageRecognition_UploadedImage",
            )

            is_submited = st.form_submit_button(
                label="Submit",
                disabled=SubmitSState.get(),
                on_click=OnSubmitHandler.lock_submit_button,
                type="primary",
            )

            error_message = ErrorMessageSState.get()
            if error_message:
                st.warning(error_message)

        if is_submited:
            try:
                form_schema = FormSchema.construct_using_form_dict(**form_dict)
            except:
                OnSubmitHandler.set_error_message(error_message="Please fill out the form completely.")
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)

            st.markdown("#### Result")
            OnSubmitHandler.display_uploaded_image(form_schema=form_schema)
            try:
                generated_answer = OnSubmitHandler.query_answer_and_display_streamly(client=client, form_schema=form_schema)
            except AuthenticationError:
                OnSubmitHandler.set_error_message(error_message="Specified OpenAI APIKey isn't valid.")
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)
            OnSubmitHandler.update_s_states(form_schema=form_schema, answer=generated_answer)
            OnSubmitHandler.reset_error_message()
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        answer = StoredAnswerSState.get()
        image_array_bgr = StoredImageSState.get()
        if answer and type(image_array_bgr) == np.ndarray:
            st.markdown("#### Result")
            st.image(
                image=image_array_bgr,
                caption=StoredPromptSState.get(),
                use_column_width=True,
            )
            st.write(answer)

        return SubComponentResult()
