import streamlit as st 
from streamlit.components.v1 import html
import base64


d = None
with open('./img/girlsalute.glb', "rb") as f:
    d = f.read()

res = f"data:@file/octet-stream;base64,{base64.b64encode(d).decode()}"

st.header("Problems In ML Safety")


streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)


html(
'''
<script type="module" src="
https://cdn.jsdelivr.net/npm/@google/model-viewer@3.5.0/dist/model-viewer.min.js
"></script>

<model-viewer camera-controls touch-action="pan-y" disable-pan autoplay src={data} style="height: 600px; width: 600px;" >
</model-viewer>

'''.format(data=res)
, width=800, height=800, scrolling=False,
)

st.write("hello")


'''
<script>
(() => {{
  const modelViewer = document.querySelector('#orbit-demo');
  const orbitCycle = [
    '45deg 55deg 4m',
    '-60deg 110deg 2m',
    modelViewer.cameraOrbit
  ];

  setInterval(() => {{
    const currentOrbitIndex = orbitCycle.indexOf(modelViewer.cameraOrbit);
    modelViewer.cameraOrbit =
        orbitCycle[(currentOrbitIndex + 1) % orbitCycle.length];
  }}, 3000);
}})();
</script>


<script type="module">
  const modelViewer2 = document.querySelector("#hotspot-camera-view-demo");
  const annotationClicked = (annotation) => {{
    let dataset = annotation.dataset;
    modelViewer2.cameraTarget = dataset.target;
    modelViewer2.cameraOrbit = dataset.orbit;
  }}

  modelViewer2.querySelectorAll('button').forEach((hotspot) => {{
    hotspot.addEventListener('click', () => annotationClicked(hotspot));
  }});
</script>


'''