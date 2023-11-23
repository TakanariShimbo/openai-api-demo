from textwrap import dedent

from openai import OpenAI
import streamlit as st

from enums.env_enum import EnvEnum


class HomeComponent:
    @classmethod
    def display_component(cls, client: OpenAI) -> None:
        api_key_type = cls.__check_api_key_type(client_api_key=client.api_key)

        content = dedent(
            f"""
            #### Overview
            Welcome to demo site of OpenAI API 🤖  
            Let's enjoy some functions 👏  

            #### API Key  
            Type: {api_key_type}  

            #### Creators  
            - Takanari Shimbo 🦥  
            - Shunichi Ikezu 🍓  
            - Yuki Yoshizawa 🤘
            """
        )
        st.markdown(content)
        st.balloons()
        # st.write(st.session_state)

    @staticmethod
    def __check_api_key_type(client_api_key: str) -> str:
        if EnvEnum.DEFAULT_OPENAI_APIKEY.value == client_api_key:
            return "server's default key"
        else:
            return "user's own key"
