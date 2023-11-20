from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.speech_generation_enum import VoiceEnum
from handlers.enum_handler import EnumHandler
from handlers.speech_generation_handler import SpeechGenerationHandler
from session_states.speech_generation_s_states import SubmitSState, ErrorMessageSState, VoiceSState, PromptSState, GeneratedSpeechSState
from components.sub_compornent_result import SubComponentResult


class FormSchema(BaseModel):
    voice_type: VoiceEnum
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
    def generate_speech(form_schema: FormSchema) -> bytes:
        speech_bytes = SpeechGenerationHandler.generate_speech(
            prompt=form_schema.prompt,
            voice=form_schema.voice_type,
        )
        return speech_bytes

    @staticmethod
    def update_s_states(
        form_schema: FormSchema,
        generated_speech_bytes: bytes,
    ) -> None:
        VoiceSState.set(value=form_schema.voice_type)
        PromptSState.set(value=form_schema.prompt)
        GeneratedSpeechSState.set(value=generated_speech_bytes)


class SpeechGenerationComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        form_dict = {}
        form = st.form(key="SpeechGeneration_PromptForm", clear_on_submit=True)
        with form:
            st.markdown("#### Prompt Form")

            form_dict["voice_type"] = st.selectbox(
                label="Voice",
                options=EnumHandler.get_enum_members(enum=VoiceEnum),
                format_func=lambda x: x.value,
                index=EnumHandler.enum_member_to_index(member=VoiceSState.get()),
                placeholder="Select voice...",
                key="SpeechGeneration_VoiceSelectBox",
            )

            form_dict["prompt"] = st.text_area(
                label="Prompt",
                disabled=SubmitSState.get(),
                placeholder="Please input prompt...",
                key="SpeechGeneration_PromptTextArea",
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

            with form:
                with st.spinner("Generating..."):
                    generated_speech_bytes = OnSubmitHandler.generate_speech(form_schema=form_schema)

            OnSubmitHandler.update_s_states(
                form_schema=form_schema,
                generated_speech_bytes=generated_speech_bytes,
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

        generated_speech = GeneratedSpeechSState.get()
        if generated_speech:
            st.markdown("#### Generated Speech")
            st.audio(data=generated_speech, format="audio/mp3")
            st.write(PromptSState.get())
        return SubComponentResult()
