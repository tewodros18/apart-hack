from random import randint
import time
import streamlit as st 
from streamlit.components.v1 import html
import base64

st.set_page_config(initial_sidebar_state="collapsed")

if 'curr' not in st.session_state:
    st.session_state['curr'] = 0

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

_Intro_talk = """
Companies are locked in a fierce race to develop the most advanced artificial intelligence systems, promising to reshape industries and redefine human potential. As you step into this digital frontier, you'll find yourself at the heart of this technological maelstrom...
"""

_second_para = """
Surrounded by screens displaying intricate AI Agents and complex algorithms.
"""
_last_para = """
To assess the potential risks and benefits of the latest AI systems vying for public deployment...
"""


if 'Name' not in st.session_state:
     st.session_state['Name'] = "Anon"

def answer_question():
    for word in _Intro_talk.split(" "):
        yield word + " "
        time.sleep(0.05)

def answer_question2():
    for word in _second_para.split(" "):
        yield word + " "
        time.sleep(0.05)
def answer_question3():
    for word in _last_para.split(" "):
        yield word + " "
        time.sleep(0.05)
def name_in():
    st.session_state['Name'] = st.session_state.namefield
    st.session_state['curr'] += 1
def change_state_up():
    st.session_state['curr'] += 1
def change_state_down():
    st.session_state['curr'] -= 1


if(st.session_state['curr'] == 0 ):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-top: 20%; font-family:\"Papyrus\";'>It's 2034, The world is on the brink of an AI revolution!</h3>
    """,
        unsafe_allow_html=True,
    )

    st.write_stream(answer_question())

    st.markdown(
    """
    <h3 style='text-align: center; color: black; font-family:\"Papyrus\";'>Insert your name</h3>
    """,
        unsafe_allow_html=True,
    )
    
    st.text_input("", "", on_change=name_in,key="namefield")

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
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col5, col4 = st.columns([4, 1])

if(st.session_state['curr'] == 1):
    st.image("./img/cartoon_id.png",)
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-top: 0%; font-family:\"Papyrus\";'>Dr. {Name}, A renowned AI safety expert, sat at the desk</h3>
    """.format(Name=st.session_state['Name']),
        unsafe_allow_html=True,
    )
    st.write_stream(answer_question2())
    st.markdown(
    """
    <h3 style='text-align: center; color: black; font-family:\"Papyrus\";'>The task was daunting:</h3>
    """.format(Name=st.session_state['Name']),
        unsafe_allow_html=True,
    )
    st.write_stream(answer_question3())


    
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
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    col1, col2, col3 = st.columns([1,3, 1])

    with col1:
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
        st.button("Back", on_click=change_state_down,key=randint(1,500))
    with col3:
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
        st.button("Continue", on_click=change_state_up,key=randint(1,500))

if(st.session_state['curr'] == 2):
    st.session_state['curr'] = 0
    st.switch_page("pages/2_board.py")