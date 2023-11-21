from textwrap import dedent

import streamlit as st


class HomeComponent:
    @staticmethod
    def display_component() -> None:
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
