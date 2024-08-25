import streamlit as st 
from streamlit.components.v1 import html
import base64

  
st.set_page_config(
    initial_sidebar_state='collapsed',
    layout = 'wide',
    page_title = 'Apart'
    
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
    body {
        font-family: Papyrus;
        background: red;
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
<h1 style='text-align: center; color: black; margin-top: 15%; font-family:\"Papyrus\";'>Unsolved Problems in AI Safety</h1>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-after {
        display: none;
    }
    .element-container:has(#button-after) {
        display: none;
    }
    .element-container:has(#button-after) + div button {
        background-color: orange;
        margin-top: 2%;
        margin-left: 47%;
        Text-font: Papyrus;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

if st.button("Explore"):
    st.switch_page("pages/1_Start.py")

    