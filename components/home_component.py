from textwrap import dedent

from openai import OpenAI
import streamlit as st


class HomeComponent:
    @staticmethod
    def display_component(client: OpenAI) -> None:
        content = dedent(
            f"""
            #### Overview
            Welcome to demo site of OpenAI API 🤖  
            Let's enjoy some functions 👏  

            #### Creators  
            - Takanari Shimbo 🦥  
            - Shunichi Ikezu 🍓  
            - Yuki Yoshizawa 🤘
            """
        )
        st.markdown(content)
        st.balloons()
        # st.write(st.session_state)
