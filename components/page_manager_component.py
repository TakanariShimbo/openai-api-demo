from openai import OpenAI
import streamlit as st

from enums.global_enum import PageEnum
from handlers.enum_handler import EnumHandler
from s_states.global_s_states import PageSState, OpenAiClientSState
from components.home_component import HomeComponent
from components.chat_gpt_component import ChatGptComponent
from components.image_recognition_component import ImageRecognitionComponent
from components.image_generation_component import ImageGenerationComponent
from components.speech_recognition_component import SpeechRecognitionComponent
from components.speech_generation_component import SpeechGenerationComponent


class PageManagerComponent:
    @classmethod
    def display_component(cls) -> None:
        st.sidebar.selectbox(
            label='Pages',
            options=EnumHandler.get_enum_members(PageEnum),
            format_func=lambda x: x.value,
            key=PageSState.get_name(),
        )

        client = OpenAiClientSState.get()
        if not client:
            st.warning("OpenAI APIKey hasn't been set yet.")
            return 
        cls.__display_selected_page(page_type=PageSState.get(), client=client)

    @staticmethod
    def __display_selected_page(page_type: PageEnum, client: OpenAI):
        st.write(f"## {page_type.value}")
        if page_type == PageEnum.HOME:
            HomeComponent.display_component(client=client)
        elif page_type == PageEnum.CHAT_GPT:
            ChatGptComponent.display_component(client=client)
        elif page_type == PageEnum.IMAGE_RECOGNITION:
            ImageRecognitionComponent.display_component(client=client)
        elif page_type == PageEnum.IMAGE_GENERATION:
            ImageGenerationComponent.display_component(client=client)
        elif page_type == PageEnum.SPEECH_RECOGNITION:
            SpeechRecognitionComponent.display_component(client=client)
        elif page_type == PageEnum.SPEECH_GENERATION:
            SpeechGenerationComponent.display_component(client=client)