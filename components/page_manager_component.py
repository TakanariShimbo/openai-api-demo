import streamlit as st

from enums.global_enum import PageEnum
from handlers.enum_handler import EnumHandler
from session_states.global_s_states import PageSState
from components.home_component import HomeComponent
from components.chat_gpt_component import ChatGptComponent
from components.image_recognition_component import ImageRecognitionComponent
from components.image_generation_component import ImageGenerationComponent
from components.speech_generation_component import SpeechGenerationComponent


class PageManagerComponent:
    @classmethod
    def display_content(cls) -> None:
        selected_page_value = st.sidebar.selectbox(
            label='Pages', 
            options=EnumHandler.get_enum_member_values(PageEnum),
            key="Global PageSelectBox",
        )
        selected_page_type = EnumHandler.value_to_enum_member(enum=PageEnum, value=selected_page_value)
        # PageSState.set(value=page_type)
        # current_page_type = PageSState.get()
        st.write(f"## {selected_page_value}")
        cls.__display_selected_page(page_type=selected_page_type)

    @staticmethod
    def __display_selected_page(page_type: PageEnum):
        if page_type == PageEnum.HOME:
            HomeComponent.display_content()
        elif page_type == PageEnum.CHAT_GPT:
            ChatGptComponent.display_component()
        elif page_type == PageEnum.IMAGE_RECOGNITION:
            ImageRecognitionComponent.display_component()
        elif page_type == PageEnum.IMAGE_GENERATION:
            ImageGenerationComponent.display_component()
        elif page_type == PageEnum.SPEECH_GENERATION:
            SpeechGenerationComponent.display_component()
