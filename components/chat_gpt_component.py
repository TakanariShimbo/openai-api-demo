from typing import Optional

from pydantic import BaseModel, ValidationError, Field
import streamlit as st

from enums.chatgpt_enum import AiModelEnum, SenderEnum
from handlers.enum_handler import EnumHandler
from handlers.chatgpt_handler import ChatGptHandler
from session_states.chat_gpt_s_states import SubmitSState, ErrorMessageSState, AiModelTypeSState, StoredHistorySState
from components.sub_compornent_result import SubComponentResult


class FormSchema(BaseModel):
    ai_model_type: AiModelEnum
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
    def display_prompt(prompt: str) -> None:
        with st.chat_message(name=SenderEnum.USER.value):
            st.write(prompt)

    @staticmethod
    def query_answer_and_display_streamly(form_schema: FormSchema) -> Optional[str]:
        if not form_schema.ai_model_type.value:
            return None

        with st.chat_message(name=form_schema.ai_model_type.value):
            answer_area = st.empty()
            answer = ChatGptHandler.query_answer_and_display_streamly(
                prompt=form_schema.prompt,
                display_func=answer_area.write,
                chat_history=StoredHistorySState.get_for_query(),
                model_type=form_schema.ai_model_type,
            )
        return answer

    @staticmethod
    def update_s_states(form_schema: FormSchema, answer: Optional[str]):
        AiModelTypeSState.set(value=form_schema.ai_model_type)
        StoredHistorySState.add(sender_type=SenderEnum.USER, sender_name=SenderEnum.USER.name, content=form_schema.prompt)
        if form_schema.ai_model_type.value and answer:
            StoredHistorySState.add(sender_type=SenderEnum.ASSISTANT, sender_name=form_schema.ai_model_type.value, content=answer)


class ChatGptComponent:
    @classmethod
    def display_component(cls) -> None:
        res = cls.__sub_component()
        if res.call_return:
            st.rerun()

    @staticmethod
    def __sub_component() -> SubComponentResult:
        history_container = st.container()
        with history_container:
            st.markdown("#### Chat History")
            for chat in StoredHistorySState.get():
                with st.chat_message(name=chat["role_name"]):
                    st.write(chat["content"])

        form_dict = {}
        form = st.form(key="ChatGpt_PromptForm", clear_on_submit=True)
        with form:
            st.markdown("#### Prompt Form")
            
            form_dict["ai_model_type"] = st.selectbox(
                label="Model",
                options=EnumHandler.get_enum_members(enum=AiModelEnum),
                format_func=lambda x: x.value,
                index=EnumHandler.enum_member_to_index(member=AiModelTypeSState.get()),
                placeholder="Select model...",
                key="ChatGpt_ModelSelectBox",
            )

            form_dict["prompt"] = st.text_area(
                label="Prompt",
                disabled=SubmitSState.get(),
                placeholder="Please input prompt...",
                key="ChatGpt_PromptTextArea",
            )

            is_submited = st.form_submit_button(
                label="Submit",
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

            with history_container:
                OnSubmitHandler.display_prompt(prompt=form_schema.prompt)
                answer = OnSubmitHandler.query_answer_and_display_streamly(form_schema=form_schema)
            OnSubmitHandler.update_s_states(form_schema=form_schema, answer=answer)
            OnSubmitHandler.reset_error_message()
            OnSubmitHandler.unlock_submit_button()
            return SubComponentResult(call_rerun=True)

        return SubComponentResult()
