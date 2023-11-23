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
        cls.__display_component_of_api_key_input()
        cls.__display_component_of_selected_page(page_type=PageSState.get())

    @classmethod
    def __display_component_of_api_key_input(cls) -> None:
        inputed_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            type="password",
            key="Sidebar_API_Key_TextInput",
        )

        if not inputed_api_key:
            OpenAiClientSState.reset()
            return
        client = OpenAiClientSState.get()
        if not client:
            OpenAiClientSState.set(value=OpenAI(api_key=inputed_api_key))
            return
        if inputed_api_key != client.api_key:
            OpenAiClientSState.set(value=OpenAI(api_key=inputed_api_key))
            return

    @staticmethod
    def __display_component_of_selected_page(page_type: PageEnum) -> None:
        client = OpenAiClientSState.get()

        if not client:
            st.warning("OpenAI API Key hasn't been set yet.")
            return

        st.sidebar.selectbox(
            label="Pages Selection",
            options=EnumHandler.get_enum_members(PageEnum),
            format_func=lambda x: x.value,
            key=PageSState.get_name(),
        )

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
