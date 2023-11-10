from typing import Optional

import streamlit as st

from enums.chatgpt_enum import ChatGptModelEnum, ChatSenderEnum
from session_states.chat_gpt_s_states import ChatGptSStates
from handlers.chatgpt_handler import ChatGptHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def on_submit_start():
        ChatGptSStates.set_submit_button_state(is_submitting=True)

    @staticmethod
    def on_submit_finish(prompt: str, answer: str):
        ChatGptSStates.set_submit_button_state(is_submitting=False)
        ChatGptSStates.add_chat_history(sender_type=ChatSenderEnum.USER, content=prompt)
        ChatGptSStates.add_chat_history(sender_type=ChatSenderEnum.ASSISTANT, content=answer)

    @staticmethod
    def on_submiting(prompt: str, selected_model_type: ChatGptModelEnum):
        with st.chat_message(name=ChatSenderEnum.USER.value):
            st.write(prompt)

        with st.chat_message(name=selected_model_type.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                display_func=answer_area.write,
                chat_history=ChatGptSStates.get_chat_history(),
                model_type=selected_model_type,
            )
        return answer


class ChatGptComponent:
    @classmethod
    def display_component(cls):
        res = cls.__step1_apply_setting()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = cls.__step2_display_chat_history()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = cls.__step3_display_new_chat()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

    @staticmethod
    def __step1_apply_setting() -> SubComponentResult:
        st.write("### Setting")
        selected_model_value = st.selectbox(
            label="Chat GPT Model",
            options=ChatGptModelEnum.to_value_list(),
            index=ChatGptModelEnum.from_type_to_index(enum=ChatGptSStates.get_model_type()),
            placeholder="Select model...",
        )

        if not selected_model_value:
            st.error("Please select model...")
            return SubComponentResult(go_next=False)
        
        selected_model_type = ChatGptModelEnum.from_value_to_type(value=selected_model_value)
        if ChatGptSStates.get_model_type() != selected_model_type:
            ChatGptSStates.set_model_type(model_type=selected_model_type)
            ChatGptSStates.reset_chat_history()
            return SubComponentResult(call_rerun=True)

        return SubComponentResult()

    @staticmethod
    def __step2_display_chat_history() -> SubComponentResult:
        st.write("### Chat History")
        for chat in ChatGptSStates.get_chat_history():
            if chat["role"] == ChatSenderEnum.USER.value:
                with st.chat_message(name=ChatSenderEnum.USER.value):
                    st.write(chat["content"])
            else:
                with st.chat_message(name=ChatGptSStates.get_model_type().value):
                    st.write(chat["content"])

        return SubComponentResult()

    @staticmethod
    def __step3_display_new_chat() -> SubComponentResult:
        inputed_prompt = st.chat_input(
            placeholder="Input prompt ...",
            on_submit=OnSubmitHandler.on_submit_start,
            disabled=ChatGptSStates.get_submit_button_state(),
        )
        if not inputed_prompt:
            return SubComponentResult()

        answer = OnSubmitHandler.on_submiting(prompt=inputed_prompt, selected_model_type=ChatGptSStates.get_model_type())
        OnSubmitHandler.on_submit_finish(prompt=inputed_prompt, answer=answer)
        return SubComponentResult(call_rerun=True)
