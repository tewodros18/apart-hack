import time
import streamlit as st 
from streamlit.components.v1 import html
import base64

st.set_page_config(
    initial_sidebar_state="collapsed",
    layout = 'wide',
    page_title = 'Apart'
    )
if 'board5State' not in st.session_state:
    st.session_state['board5State'] = 0
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
    st.session_state['board5State'] += 1
def change_state_down():
    st.session_state['board5State'] -= 1





if(st.session_state['board5State'] == 0):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'>Agent No. 2: Grid Master</h3>
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
            - Deployed to manage public transit system
            - Expected to prevent 20,000 fatalities
            - Reduces carbon footprint from gridlocks
            - Dynamic Traffic Signal Optimization
            - Pothole Detection and Repair
        """, icon="🤖")
        st.success("""
        Safety Information:\n
            - Robust Ethical Framework 
            - human notification for black swans and anomalies  
            - Another "Big Red" termination button 
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


        st.button("20k lives,Deploy!", on_click=change_state_up)
if(st.session_state['board5State'] == 1):
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
        st.image("./img/traffic2.png")
        st.markdown(
        """
        <h3 style='text-align: center; color: red;  font-family:\"Papyrus\";'>Ohhhh No!!</h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>An Attacker triggered a hidden functionality to increase traffic congestion slightly in selected areas.</h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: red;  font-family:\"Papyrus\";'>Coincidentally *wink wink*
</h3>
        """,
            unsafe_allow_html=True,
        )
        st.markdown(
        """
        <h3 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Today was election day and this affected voter turn out in selected areas</h3>
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

        

if(st.session_state['board5State'] == 2):
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
        <h3 style='text-align: center; color: black;margin-bottom:5%;  font-family:\"Papyrus\";'></h3>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
        """
        <h5 style='text-align: center; color: black;  font-family:\"Papyrus\";'>Machine learning systems risk carrying hidden “backdoor” or “trojan” controllable vulnerabilities. Backdoored models behave correctly and benignly in almost all scenarios, but in particular circumstances
        chosen by an adversary, they have been taught to behave incorrectly.</h5>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
        """
        <h5 style='text-align: center; color: black;  font-family:\"Papyrus\";'>To avoid deploying models that may take unexpected turns and have vulnerabilities that can be
    controlled by an adversary, researchers could improve backdoor detectors</h5>""",
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
if(st.session_state['board5State'] == 3):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-top:15%; font-family:\"Papyrus\";'>Alignment seems very difficult! Maybe we should use AI to solve it</h3>
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
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


    st.button("Tell me more!", on_click=change_state_up)
if(st.session_state['board5State'] == 4):
    st.markdown(
    """
    <h3 style='text-align: center; color: black; margin-bottom:2%; font-family:\"Papyrus\";'>Introducing HAL ! Your Trusted AI safety helper</h3>
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
        st.markdown(
        """
        <h5 style='text-align: center; color: black; margin-top:25%; font-family:\"Papyrus\";'>Train HAL on all previous incidents to distill AI Safety principles</h5>
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
                text-font: Papyrus;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)


        st.button("Proceed", on_click=change_state_up)

if(st.session_state['board5State'] == 5):
    progress_text = "Training in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(70):
        time.sleep(0.02)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.session_state['board5State'] = 0
    st.switch_page("pages/6_board.py")