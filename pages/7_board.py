import time
import streamlit as st 
from streamlit.components.v1 import html
import base64

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout = 'wide',
    page_title = 'Apart'
    )
if 'board7State' not in st.session_state:
    st.session_state['board7State'] = 0
if 'Name' not in st.session_state:
    st.session_state['Name'] = "You"
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

def change_state_up():
    st.session_state['board7State'] += 1
def change_state_down():
    st.session_state['board7State'] -= 1

if(st.session_state['board5State'] == 0):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'>HAL picked up the wrong idea!</h3>
    """,
        unsafe_allow_html=True,
    )
    col1, col2,col3 = st.columns([3, 2,1])
    with col1:
        st.image("./img/glitch.gif")
    with col2:
        st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>In order to ensure safety, I must learn through failure without being turned off!</h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: red;  font-family:\"Papyrus\";'>Yet, You hold the Big Red Button
        </h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Initiate reputation destruction...Target is </h3>
        """.format(Name=st.session_state['Name']),
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: red;  font-family:\"Papyrus\";'>Dr. {Name}
        </h3>
        """.format(Name=st.session_state['Name']),
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
                margin-top: 8%;
                margin-left: 47%;
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


        st.button("Finish", on_click=change_state_up)
if(st.session_state['board5State'] == 1):
    st.session_state['board5State'] = 0
    st.switch_page("1_home.py")