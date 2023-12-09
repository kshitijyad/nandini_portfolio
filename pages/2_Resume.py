import streamlit as st
import base64
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

image_path = "images/nandini.jpg"

def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
# URL to link to
link_url = "https://www.linkedin.com/in/nandinicomar/"

encoded_image = get_image_base64(image_path)
html_code = f"""
    <a href="{link_url}" target="_blank">
        <img src="data:image/jpeg;base64,{encoded_image}" alt="Clickable Image" style="width:100%">
    </a>
"""

# Display the clickable image in the sidebar
st.sidebar.markdown(html_code, unsafe_allow_html=True)

st.title("📝 Resume")

st.write("[Click here if it's blocked by your browser](https://cognitiveclass.ai/)")

with open("data/Resume_Nandini_Comar.pdf","rb") as f:
      base64_pdf = base64.b64encode(f.read()).decode('utf-8')
      pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
      st.markdown(pdf_display, unsafe_allow_html=True)
  
