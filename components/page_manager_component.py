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
        st.sidebar.selectbox(
            label='Pages',
            options=EnumHandler.get_enum_members(PageEnum),
            format_func=lambda x: x.value,
            key=PageSState.get_name(),
        )

        st.write(f"## {PageSState.get()}")
        cls.__display_selected_page(page_type=PageSState.get())

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
