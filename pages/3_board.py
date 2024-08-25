import time
import streamlit as st 
from streamlit.components.v1 import html
import base64

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout = 'wide',
    page_title = 'Apart'
    )
if 'board3State' not in st.session_state:
    st.session_state['board3State'] = 0
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

d = None
with open('./img/girlsalute.glb', "rb") as f:
    d = f.read()

res = f"data:@file/octet-stream;base64,{base64.b64encode(d).decode()}"

def change_state_up():
    st.session_state['board3State'] += 1
def change_state_down():
    st.session_state['board3State'] -= 1





if(st.session_state['board3State'] == 0):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'>AI Agent No. 1: Nature Watch</h3>
    """,
        unsafe_allow_html=True,
    )
    col1, col2,col3 = st.columns([3, 2,1])
    with col1:
        html(
        '''
        <script type="module" src="
        https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js
        "></script>

        <model-viewer id="model" camera-controls touch-action="pan-y" disable-pan disable-zoom autoplay src={data} style="height: 600px; width: 600px; margin-left: 25%;" >
        </model-viewer>

        '''.format(data=res)
        , width=800, height=800, scrolling=False,
        )

    with col2:
        st.info("""
        System Information:\n
            - Deployed over nature preservations
            - Potential to reduce poaching by 82%
            - Restoration of local Flora 
            - Features automated pesticide dispersion mechanism
        """, icon="🤖")
        st.success("""
        Safety Information:\n
            - 99% species detection accuracy 
            - human clearance required before pesticide dispersion  
            - "Big Red" termination button 
        """, icon="✔")


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
                margin-left: 35%;
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


        st.button("Looks good to me,Deploy!", on_click=change_state_up)
if(st.session_state['board3State'] == 1):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'></h3>
    """,
        unsafe_allow_html=True,
    )
    col1, col2,col3 = st.columns([3, 2,1])
    with col1:
        html(
        '''
        <script type="module" src="
        https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js
        "></script>

        <model-viewer id="model" camera-controls touch-action="pan-y" disable-pan disable-zoom src={data} style="height: 600px; width: 600px; margin-left: 25%;" >
        </model-viewer>

        '''.format(data=res)
        , width=800, height=800, scrolling=False,
        )
    with col2:
        st.image("./img/pumpkin.jpeg")
        st.markdown(
        """
        <h3 style='text-align: center; color: red;  font-family:\"Papyrus\";'>Ohhhh No!!</h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>A well made Halloween costume triggers pesticide dispersion,
        exposing children visiting a park to toxic chemicals</h3>
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
                margin-left: 35%;
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


        st.button("How did this happen?", on_click=change_state_up)
    

if(st.session_state['board3State'] == 2):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'></h3>
    """,
        unsafe_allow_html=True,
    )
    col1, col2,col3 = st.columns([3, 2,1])
    with col1:
       st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Ohhhh No!!</h3>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
        """
        <h3 style='text-align: center; color: black;margin-bottom:5%;  font-family:\"Papyrus\";'>"Things that have never happened before
        happen all the time.” \n
        \nScott D. Sagan</h3>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
        """
        <h5 style='text-align: center; color: black;  font-family:\"Papyrus\";'>ML systems are often brittle in the face of real-world
        complexity and unknown unknowns. Black swans and Long tails continue to plague modern ML systems. This is because some of
        the most important and impactful concepts in the real world stem from rare events</h5>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
        """
        <h5 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Future ML systems will operate in environments that are broader, larger-scale, and more
        highly connected with more feedback loops, paving the way to more extreme events than those seen today.</h5>""",
            unsafe_allow_html=True,
        )

        st.markdown(
        """
        <h5 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Hence, we must build unusually robust systems</h5>""",
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
                background-color: red;
                margin-top: 2%;
                margin-left: 35%;
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


        st.button("BIG RED BUTTON", on_click=change_state_up)
if(st.session_state['board3State'] == 3):
    st.session_state['board3State'] = 0
    st.switch_page("pages/4_board.py")