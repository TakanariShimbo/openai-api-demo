from textwrap import dedent

import streamlit as st


class HomeComponent:
    @staticmethod
    def display_content() -> None:
        content = dedent(
            f"""
            Welcome to demo site of OpenAI API 🤖  
            Let's enjoy OpenAI API 👏  


            **Creators**  
            - Takanari Shimbo 🦥  
            - Shunichi Ikezu 🍓  
            - Yuki Yoshizawa 🤘
            """
        )
        st.markdown(content)
        st.balloons()
