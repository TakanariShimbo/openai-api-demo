from openai import OpenAI, AuthenticationError
from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.speech_generation_enum import VoiceEnum
from handlers.enum_handler import EnumHandler
from handlers.speech_generation_handler import SpeechGenerationHandler
from s_states.speech_generation_s_states import SubmitSState, ErrorMessageSState, VoiceTypeSState, StoredPromptSState, StoredSpeechSState
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
    def set_error_message(error_message: str) -> None:
        ErrorMessageSState.set(value=error_message)

    @staticmethod
    def reset_error_message() -> None:
        ErrorMessageSState.reset()

    @staticmethod
    def generate_speech(client: OpenAI, form_schema: FormSchema) -> bytes:
        speech_bytes = SpeechGenerationHandler.generate_speech(
            client=client,
            prompt=form_schema.prompt,
            voice_type=form_schema.voice_type,
        )
        return speech_bytes

    @staticmethod
    def update_s_states(
        form_schema: FormSchema,
        speech_bytes: bytes,
    ) -> None:
        VoiceTypeSState.set(value=form_schema.voice_type)
        StoredPromptSState.set(value=form_schema.prompt)
        StoredSpeechSState.set(value=speech_bytes)


class SpeechGenerationComponent:
    @classmethod
    def display_component(cls, client: OpenAI) -> None:
        res = cls.__sub_component(client=client)
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component(client: OpenAI) -> SubComponentResult:
        form_dict = {}
        form = st.form(key="SpeechGeneration_Form", clear_on_submit=True)
        with form:
            st.markdown("#### Form")

            form_dict["voice_type"] = st.selectbox(
                label="Voice",
                options=EnumHandler.get_enum_members(enum=VoiceEnum),
                format_func=lambda x: x.name,
                index=EnumHandler.enum_member_to_index(member=VoiceTypeSState.get()),
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
                form_schema = FormSchema(**form_dict)
            except ValidationError:
                OnSubmitHandler.set_error_message(error_message="Please fill out the form completely.")
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)

            with form:
                with st.spinner("Generating..."):
                    try:
                        generated_speech_bytes = OnSubmitHandler.generate_speech(client=client, form_schema=form_schema)
                    except AuthenticationError:
                        OnSubmitHandler.set_error_message(error_message="Specified OpenAI APIKey isn't valid.")
                        OnSubmitHandler.unlock_submit_button()
                        return SubComponentResult(call_rerun=True)

            OnSubmitHandler.update_s_states(
                form_schema=form_schema,
                speech_bytes=generated_speech_bytes,
            )

            OnSubmitHandler.reset_error_message()
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        speech_bytes = StoredSpeechSState.get()
        if speech_bytes:
            st.markdown("#### Result")
            st.audio(data=speech_bytes, format="audio/mp3")
            st.write(StoredPromptSState.get())
        return SubComponentResult()
