from typing import Optional

import streamlit as st

from enums.sender_enum import SenderEnum
from enums.chatgpt_enum import ChatGptEnum
from session_states.chat_gpt_session_states import ChatGptSessionStates
from handlers.chatgpt_handler import ChatGptHandler
from components.base import SubComponentResult


class OnSubmitHandler:
    @staticmethod
    def on_submit_start():
        ChatGptSessionStates.set_submit_button_state(is_submitting=True)

    @staticmethod
    def on_submit_finish(prompt: str, answer: str):
        ChatGptSessionStates.set_submit_button_state(is_submitting=False)
        ChatGptSessionStates.add_chat_history(sender_type=SenderEnum.USER, content=prompt)
        ChatGptSessionStates.add_chat_history(sender_type=SenderEnum.ASSISTANT, content=answer)

    @staticmethod
    def on_submiting(prompt: str, selected_model_enum: ChatGptEnum):
        with st.chat_message(name=SenderEnum.USER.value):
            st.write(prompt)

        with st.chat_message(name=selected_model_enum.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                display_func=answer_area.write,
                original_chat_history=ChatGptSessionStates.get_chat_history(),
                model_type=selected_model_enum,
            )
        return answer


class ChatGptComponent:
    def __init__(self) -> None:
        self.__selected_model_enum: Optional[ChatGptEnum]

    def display_component(self):
        res = self.__step1_setting()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = self.__step2_apply_setting()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = self.__step3_display_chat_history()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

        res = self.__step4_display_new_chat()
        if not res.go_next:
            return
        if res.call_return:
            st.rerun()
            return

    def __step1_setting(self) -> SubComponentResult:
        st.write("### Setting")
        selected_model_value = st.selectbox(
            label="Chat GPT Model",
            options=ChatGptEnum.to_value_list(),
            index=ChatGptEnum.from_enum_to_index(enum=ChatGptSessionStates.get_model_type()),
            placeholder="Select model...",
        )

        if not selected_model_value:
            st.error("Please select model...")
            return SubComponentResult(go_next=False)
        
        selected_model_enum = ChatGptEnum.from_value_to_enum(value=selected_model_value)
        self.__selected_model_enum = selected_model_enum
        return SubComponentResult()

    def __step2_apply_setting(self) -> SubComponentResult:
        selected_model_enum = self.__selected_model_enum
        if not selected_model_enum:
            st.error("error...")
            return SubComponentResult(go_next=False)

        if ChatGptSessionStates.get_model_type() != selected_model_enum:
            ChatGptSessionStates.set_model_type(model_type=selected_model_enum)
            ChatGptSessionStates.reset_chat_history()
            return SubComponentResult(call_rerun=True)

        return SubComponentResult()

    def __step3_display_chat_history(self) -> SubComponentResult:
        selected_model_enum = self.__selected_model_enum
        if not selected_model_enum:
            st.error("error...")
            return SubComponentResult(go_next=False)

        st.write("### Chat History")
        for chat in ChatGptSessionStates.get_chat_history():
            if chat["role"] == SenderEnum.USER.value:
                with st.chat_message(name=SenderEnum.USER.value):
                    st.write(chat["content"])
            else:
                with st.chat_message(name=selected_model_enum.value):
                    st.write(chat["content"])

        return SubComponentResult()

    def __step4_display_new_chat(self) -> SubComponentResult:
        selected_model_enum = self.__selected_model_enum
        if not selected_model_enum:
            st.error("error...")
            return SubComponentResult(go_next=False)

        inputed_prompt = st.chat_input(
            placeholder="Input prompt ...",
            on_submit=OnSubmitHandler.on_submit_start,
            disabled=ChatGptSessionStates.get_submit_button_state(),
        )
        if not inputed_prompt:
            return SubComponentResult()

        answer = OnSubmitHandler.on_submiting(prompt=inputed_prompt, selected_model_enum=selected_model_enum)
        OnSubmitHandler.on_submit_finish(prompt=inputed_prompt, answer=answer)
        return SubComponentResult(call_rerun=True)
