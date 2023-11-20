import streamlit as st


class ConfigComponent:
    @staticmethod
    def set_page_configs() -> None:
        st.set_page_config(
            page_title="OpenAI API Demo",
            page_icon="🤖",
        )