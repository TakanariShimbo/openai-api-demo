from textwrap import dedent

import streamlit as st

from components.title_component import TitleComponent


"""
TITLE
"""
TitleComponent.set_page_configs(
    icon="🏠",
    title="home",
)


"""
CONTENTS
"""
def display_content() -> None:
    content = dedent(
        f"""
        Welcome to demo site of OpenAI API 🤖  
        Let's enjoy OpenAI API 👏  
        """
    )
    st.markdown(content)
    st.balloons()

display_content()