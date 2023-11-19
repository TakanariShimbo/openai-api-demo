from typing import Optional

from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.chatgpt_enum import ModelEnum, SenderEnum
from session_states.chat_gpt_s_states import SubmitSState, ErrorMessageSState, ModelSState, ChatHistorySState
from handlers.enum_handler import EnumHandler
from handlers.chatgpt_handler import ChatGptHandler
from components.base import SubComponentResult


class FormSchema(BaseModel):
    model_value: str
    prompt: str = Field(min_length=1)

    @property
    def model_type(self) -> ModelEnum:
        return EnumHandler.value_to_enum_member(enum=ModelEnum, value=self.model_value)


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
    def display_prompt(prompt: str) -> None:
        with st.chat_message(name=SenderEnum.USER.value):
            st.write(prompt)

    @staticmethod
    def query_and_display_answer(form_schema: FormSchema) -> Optional[str]:
        if not form_schema.model_type.value:
            return None

        with st.chat_message(name=form_schema.model_type.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=form_schema.prompt,
                display_func=answer_area.write,
                chat_history=ChatHistorySState.get_for_query(),
                model_type=form_schema.model_type,
            )
        return answer

    @staticmethod
    def update_s_states(form_schema: FormSchema, answer: Optional[str]):
        ModelSState.set(value=form_schema.model_type)
        ChatHistorySState.add(sender_type=SenderEnum.USER, sender_name=SenderEnum.USER.name, content=form_schema.prompt)
        if form_schema.model_type.value and answer:
            ChatHistorySState.add(sender_type=SenderEnum.ASSISTANT, sender_name=form_schema.model_type.value, content=answer)


class ChatGptComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        form_dict = {}

        st.write("### Setting")
        form_dict["model_value"] = st.selectbox(
            label="Model",
            options=EnumHandler.get_enum_member_values(enum=ModelEnum),
            index=EnumHandler.enum_member_to_index(member=ModelSState.get()),
            placeholder="Select model...",
            key="ChatGpt ModelSelectBox",
        )

        st.write("### Chat History")
        for chat in ChatHistorySState.get():
            with st.chat_message(name=chat["role_name"]):
                st.write(chat["content"])

        form_dict["prompt"] = st.chat_input(
            placeholder="Input prompt ...",
            on_submit=OnSubmitHandler.lock_submit_button,
            disabled=SubmitSState.get(),
            key="ChatGpt ChatInput",
        )

        if form_dict["prompt"]:
            try:
                form_schema = FormSchema(**form_dict)
            except ValidationError:
                OnSubmitHandler.set_error_message()
                OnSubmitHandler.unlock_submit_button()
                return SubComponentResult(call_rerun=True)

            OnSubmitHandler.display_prompt(prompt=form_schema.prompt)
            answer = OnSubmitHandler.query_and_display_answer(form_schema=form_schema)
            OnSubmitHandler.update_s_states(form_schema=form_schema, answer=answer)
            OnSubmitHandler.reset_error_message()
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        return SubComponentResult()
