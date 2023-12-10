import streamlit as st
import base64

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

st.title("Transcripts 🗄️")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")
# Function to create a download button for a PDF
def create_download_button(pdf_file_path, button_text):
    with open(pdf_file_path, "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    href = f'<a href="data:file/pdf;base64,{base64_pdf}" download="{pdf_file_path}" style="text-decoration: none;">{button_text}</a>'
    st.markdown(href, unsafe_allow_html=True)

# Display download links for the transcripts
st.header("Masters: LLM - Fordham Law Transcripts")
create_download_button("data/Masters_LLM_Fordham LLM Transcript.pdf", "Download Fordham Transcripts")

st.header("Bachelors: LLb - IIT Khargapur Transcripts")
create_download_button("data/Bachelor_LLB_IIT KGP Transcripts.pdf", "Download IIT Transcripts")
