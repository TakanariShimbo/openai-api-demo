import streamlit as st

from enums.sender_enum import SenderEnum
from enums.chatgpt_enum import ChatGptEnum
from handlers.session_state_handler import SessionStateHandler
from handlers.chatgpt_handler import ChatGptHandler
from components.title_component import TitleComponent


class OnSubmitHandler:
    @staticmethod
    def on_submit_start():
        SessionStateHandler.set_chat_submit_button_state(is_submitting=True)

    @staticmethod
    def on_submit_finish(prompt: str, answer: str):
        SessionStateHandler.set_chat_submit_button_state(is_submitting=False)
        SessionStateHandler.add_chat_history(sender_type=SenderEnum.USER, content=prompt)
        SessionStateHandler.add_chat_history(sender_type=SenderEnum.ASSISTANT, content=answer)

    @staticmethod
    def on_submiting(prompt: str):
        with st.chat_message(name=SenderEnum.USER.value):
            st.write(prompt)

        with st.chat_message(name=selected_model_enum.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_and_display_answer_streamly(
                prompt=prompt,
                display_func=answer_area.write,
                original_chat_history=SessionStateHandler.get_chat_history(),
                model_type=selected_model_enum,
            )
        return answer


# Set Titles
TitleComponent.set_page_configs(
    icon="💬",
    title="ChatGPT",
)


# display model setting
st.write("### Model Setting")
selected_model_value = st.selectbox(
    label="ChatGPT Model",
    options=ChatGptEnum.to_value_list(),
    index=SessionStateHandler.get_chat_model_index(),
    placeholder="Select model...",
)

if not selected_model_value:
    st.error("Please select model...")

else:
    selected_model_enum = ChatGptEnum.from_value_to_enum(value=selected_model_value)
    selected_model_index = ChatGptEnum.from_value_to_index(value=selected_model_value)

    # delete chat history if model changed
    if SessionStateHandler.get_chat_model_index() != selected_model_index:
        SessionStateHandler.set_chat_model_index(model_index=selected_model_index)
        SessionStateHandler.reset_chat_history()
        st.rerun()

    # display chat history
    st.write("### Chat History")
    for chat in SessionStateHandler.get_chat_history():
        if chat["role"] == SenderEnum.USER.value:
            with st.chat_message(name=SenderEnum.USER.value):
                st.write(chat["content"])
        else:
            with st.chat_message(name=selected_model_enum.value):
                st.write(chat["content"])

    inputed_prompt = st.chat_input(
        placeholder="Input prompt ...",
        on_submit=OnSubmitHandler.on_submit_start(),
        disabled=not SessionStateHandler.get_chat_submit_button_state(),
    )
    if inputed_prompt:
        answer = OnSubmitHandler.on_submiting(prompt=inputed_prompt)
        OnSubmitHandler.on_submit_finish(prompt=inputed_prompt, answer=answer)
        st.rerun()
