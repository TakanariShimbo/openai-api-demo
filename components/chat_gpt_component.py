import streamlit as st

from enums.chatgpt_enum import ChatGptModelEnum, ChatSenderEnum
from session_states.chat_gpt_s_states import ChatGptSStates
from handlers.enum_handler import EnumHandler
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
    def display_prompt(prompt: str) -> None:
        with st.chat_message(name=ChatSenderEnum.USER.value):
            st.write(prompt)

    @staticmethod
    def query_and_display_answer(prompt: str, selected_model_type: ChatGptModelEnum) -> str:
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
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        st.write("### Setting")
        selected_model_value = st.selectbox(
            label="Model",
            options=EnumHandler.get_enum_member_values(enum=ChatGptModelEnum),
            index=EnumHandler.enum_member_to_index(member=ChatGptSStates.get_model_type()),
            placeholder="Select model...",
            key="ChatModelSelectBox",
        )

        if not selected_model_value:
            st.warning("Please select model...")
            return SubComponentResult()

        selected_model_type = EnumHandler.value_to_enum_member(enum=ChatGptModelEnum, value=selected_model_value)
        if ChatGptSStates.get_model_type() != selected_model_type:
            ChatGptSStates.set_model_type(model_type=selected_model_type)
            ChatGptSStates.reset_chat_history()
            return SubComponentResult(call_rerun=True)

        st.write("### Chat History")
        for chat in ChatGptSStates.get_chat_history():
            if chat["role"] == ChatSenderEnum.USER.value:
                with st.chat_message(name=ChatSenderEnum.USER.value):
                    st.write(chat["content"])
            else:
                with st.chat_message(name=ChatGptSStates.get_model_type().value):
                    st.write(chat["content"])

        inputed_prompt = st.chat_input(
            placeholder="Input prompt ...",
            on_submit=OnSubmitHandler.on_submit_start,
            disabled=ChatGptSStates.get_submit_button_state(),
            key="ChatInput",
        )
        if inputed_prompt:
            OnSubmitHandler.display_prompt(prompt=inputed_prompt)
            answer = OnSubmitHandler.query_and_display_answer(prompt=inputed_prompt, selected_model_type=ChatGptSStates.get_model_type())
            OnSubmitHandler.on_submit_finish(prompt=inputed_prompt, answer=answer)
            return SubComponentResult(call_rerun=True)
        
        return SubComponentResult()


