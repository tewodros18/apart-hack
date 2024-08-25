import time
import streamlit as st 
from streamlit.components.v1 import html
import base64

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout = 'wide',
    page_title = 'Apart'
    )

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    body {
        font-family: Papyrus;
    }
    input[type=button] {
        font-family: Papyrus;

    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<h1 style='text-align: center; color: black; margin-top: 15%; font-family:\"Papyrus\";'>Chapter One: Robustness</h1>
""",
    unsafe_allow_html=True,
)

time.sleep(1.5)

st.switch_page("pages/3_board.py")