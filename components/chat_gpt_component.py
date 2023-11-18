from typing import Optional

import streamlit as st

from enums.chatgpt_enum import ModelEnum, SenderEnum
from session_states.chat_gpt_s_states import SubmitSState, ModelSState, ChatHistorySState
from handlers.enum_handler import EnumHandler
from handlers.chatgpt_handler import ChatGptHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def lock_submit_button():
        SubmitSState.set(value=True)

    @staticmethod
    def unlock_submit_button():
        SubmitSState.set(value=False)

    @staticmethod
    def display_prompt(prompt: str) -> None:
        with st.chat_message(name=SenderEnum.USER.value):
            st.write(prompt)

    @staticmethod
    def query_and_display_answer(prompt: str, selected_model_type: ModelEnum) -> Optional[str]:
        if not selected_model_type.value:
            return None
        
        with st.chat_message(name=selected_model_type.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                display_func=answer_area.write,
                chat_history=ChatHistorySState.get_for_query(),
                model_type=selected_model_type,
            )
        return answer

    @staticmethod
    def update_s_states(prompt: str, answer: Optional[str], model_type: ModelEnum):
        ModelSState.set(value=model_type)        
        ChatHistorySState.add(sender_type=SenderEnum.USER, sender_name=SenderEnum.USER.name, content=prompt)
        if model_type.value and answer:
            ChatHistorySState.add(sender_type=SenderEnum.ASSISTANT, sender_name=model_type.value, content=answer)


class ChatGptComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        st.write("### Setting")
        selected_model_value = st.selectbox(
            label="Model",
            options=EnumHandler.get_enum_member_values(enum=ModelEnum),
            index=EnumHandler.enum_member_to_index(member=ModelSState.get()),
            placeholder="Select model...",
            key="ChatGpt ModelSelectBox",
        )
        selected_model_type = EnumHandler.value_to_enum_member(enum=ModelEnum, value=selected_model_value)

        st.write("### Chat History")
        for chat in ChatHistorySState.get():
            with st.chat_message(name=chat["role_name"]):
                st.write(chat["content"])

        inputed_prompt = st.chat_input(
            placeholder="Input prompt ...",
            on_submit=OnSubmitHandler.lock_submit_button,
            disabled=SubmitSState.get(),
            key="ChatGpt ChatInput",
        )
        if inputed_prompt:
            OnSubmitHandler.display_prompt(prompt=inputed_prompt)
            answer = OnSubmitHandler.query_and_display_answer(prompt=inputed_prompt, selected_model_type=selected_model_type)
            OnSubmitHandler.update_s_states(prompt=inputed_prompt, answer=answer, model_type=selected_model_type)
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)
        
        return SubComponentResult()


