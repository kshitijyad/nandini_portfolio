import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from PIL import Image
from openai import OpenAI
import base64
import os


st.set_page_config(page_title='Nandini Comar' ,layout="wide",page_icon='👧🏻')
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from PIL import Image
from openai import OpenAI
import base64
import os

def apply_custom_css():
    st.markdown("""
    <style>
    /* Global Styles */
    body {
        color: #333333;
        background-color: #FFFFFF;
        font-family: Arial, sans-serif;
    }

    /* Header Styles */
    h1, h2, h3 {
        color: #1E3A8A;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    h1 {
        font-size: 2.5em;
    }

    h2 {
        font-size: 2em;
    }

    h3 {
        font-size: 1.5em;
    }

    /* Paragraph and Text Styles */
    p, li, .stMarkdown {
        font-size: 16px;
        line-height: 1.6;
        color: #1F2937;
    }

    /* Button Styles */
    .stButton > button {
        color: #FFFFFF;
        background-color: #3B82F6;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #2563EB;
    }

    /* Input Field Styles */
    .stTextInput > div > div > input {
        color: #1F2937;
        background-color: #F3F4F6;
        border: 1px solid #D1D5DB;
        padding: 10px;
        border-radius: 4px;
    }

    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background-color: #F3F4F6;
        padding: 20px;
    }

    [data-testid="stSidebar"] [data-testid="stImage"] {
        margin-bottom: 20px;
    }

    /* Link Styles */
    a {
        color: #3B82F6;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Custom Classes */
    .gradient-header {
        background: linear-gradient(to right, #3B82F6, #60A5FA);
        color: white;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .response-box {
        background-color: #F3F4F6;
        border: 1px solid #D1D5DB;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }

    /* Icon Styles */
    i.fa, i.fas, i.far, i.fab {
        margin-right: 5px;
    }

    /* Timeline Styles */
    .timeline {
        margin-top: 30px;
        margin-bottom: 30px;
    }

    /* Endorsement Styles */
    .endorsement {
        background-color: #F3F4F6;
        border: 1px solid #D1D5DB;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
   /* Add this new style for markdown text */
    .stMarkdown, .stMarkdown p {
        color: #333333 !important;  /* Dark gray color for better contrast */
        font-size: 16px;
        line-height: 1.6;
    }

    /* You might also want to style markdown links separately */
    .stMarkdown a {
        color: #3B82F6 !important;  /* Blue color for links */
        text-decoration: none;
    }

    .stMarkdown a:hover {
        text-decoration: underline;
    }
    /* Add this new style for the spinner */
    .stSpinner > div > div {
        color: black !important;
    }

    /* If you also want to change the spinner icon color */
    .stSpinner > div > div > div {
        border-top-color: black !important;
    }
    /* Rest of your existing styles... */
    </style>
    """, unsafe_allow_html=True)


apply_custom_css()

# -----------------  chatbot  ----------------- #
# Set up the OpenAI key

pronoun = info["Pronoun"]
name = info["Name"]

# -----------------  loading assets  ----------------- #
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

    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")



# ----------------- info ----------------- #
full_name = info['Full_Name']

def gradient(color1, color2, color3, content1, content2):
    st.markdown(f"""
    <h1 style="text-align:center; background-image: linear-gradient(to right, {color1}, {color2}); 
                font-size:60px; border-radius:2%; box-shadow: 0px 2px 5px rgba(0,0,0,0.2); color:{color3};">
        <span style="text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">{content1}</span><br>
        <span style="color:white; font-size:18px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);">{content2}</span>
    </h1>
    """, unsafe_allow_html=True)

# Updated colors for better contrast
gradient('#4aaada','#d3ba42', 'black', f"Hi, I'm {full_name}👋", info["Intro"])


with st.container():
    col1, col2 = st.columns(2)

    bullet_points = [
        "Experienced attorney specializing in <b style='color: #4aaada;'>commercial contracts</b> and <b style='color: #4aaada;'>technology agreements</b> with <b style='color: #4aaada;'>5+ years</b> of expertise",
        "Negotiated and drafted <b style='color: #4aaada;'>over 100 contracts</b>, including software, SaaS, data license, and professional services agreements",
        "Excel at developing <b style='color: #4aaada;'>strategic partnerships</b> with business leaders and implementing best practices",
        "Advise on <b style='color: #4aaada;'>complex legal issues</b> and risks in technology and commercial contexts",
        "Managed IP portfolios for <b style='color: #4aaada;'>25+ clients</b>, reducing infringement incidents by <b style='color: #4aaada;'>90%</b>",
        "Experienced in navigating <b style='color: #4aaada;'>patent litigation</b> and IP protection strategies",
        "Adept at translating complex legal concepts into <b style='color: #4aaada;'>clear, actionable insights</b> for non-legal stakeholders",
        "Strong skills in <b style='color: #4aaada;'>contract compliance</b>, <b style='color: #4aaada;'>risk mitigation</b>, and <b style='color: #4aaada;'>cross-functional collaboration</b>",
        "Well-suited to support <b style='color: #4aaada;'>financial intelligence</b>, <b style='color: #4aaada;'>data analytics</b>, and <b style='color: #4aaada;'>software services</b> businesses",
        "Keen interest and expertise in <b style='color: #ec1458; text-decoration: underline;'>GenAI</b>, <b style='color: #ec1458; text-decoration: underline;'>legal operations</b>, and <b style='color: #ec1458; text-decoration: underline;'>legal tech innovations</b>, with a proven ability to implement cutting-edge solutions"

    ]

    mid_point = len(bullet_points) // 2 + len(bullet_points) % 2

    with col1:
        st.markdown(f"""
            <div style="font-size:18px; line-height: 1.6;">
                <ul>
                    {"".join(f"<li>{point}</li>" for point in bullet_points[:mid_point-1])}
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style="font-size:18px; line-height: 1.6;">
                <ul>
                    {"".join(f"<li>{point}</li>" for point in bullet_points[mid_point-1:])}
                </ul>
            </div>
        """, unsafe_allow_html=True)
# ----------------- Llama ----------------- #
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_documents(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):  # Assuming text files
            with open(os.path.join(directory, filename), 'r') as file:
                documents.append(file.read())
    return documents

def split_text(text, max_chunk_size=1000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        if current_size + len(word) > max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_size = len(word)
        else:
            current_chunk.append(word)
            current_size += len(word) + 1  # +1 for space
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

# Load and process documents
documents = load_documents("data")
all_chunks = []
for doc in documents:
    all_chunks.extend(split_text(doc))

def find_relevant_chunks(query, chunks, top_n=3):
    # This is a very basic relevance function. You might want to use a more sophisticated method.
    return sorted(chunks, key=lambda x: -sum(query.lower().count(word.lower()) for word in x.split()))[:top_n]

# Function to generate response using OpenAI API
def generate_response(query, context):
    prompt = f"""We have provided context information below. 
---------------------
{context}
---------------------
Given this information, please answer the question and follow these guidelines when answering:

1. Each answer should be tastefully written in a bullet point format.
2. Add new lines between major points for readability.
3. Use emojis to make the answer more engaging, but don't overuse them.
4. The answer should be comprehensive and detailed, aiming for at least 200-300 words.
5. VERY IMPORTANT: You are replying to a potential hiring manager or recruiter, so make sure you word the answer in a way that appeals to them. Highlight Nandini's achievements, skills, and potential value to the company.
6. Use Markdown formats to highlight and underline important parts of the reply. Use **bold** for key skills or achievements, and *italics* for supporting details.
7. When the question contains multiple parts, create a header for each part using Markdown (##), and list your answer below it. For example:

For the question: "Can you elaborate on Nandini's specialization in intellectual property law and how she has applied it in her past roles?"

## Nandini's Specialization in Intellectual Property Law
[Answer this part]

## Application of IP Law in Past Roles
[Answer this part]

8. Use bullet points (-) for main points and sub-bullets (  •) for additional details.
9. Include specific examples, metrics, or achievements whenever possible to substantiate claims.
10. Conclude each section with a brief statement on how Nandini's experience or skills in that area would benefit a potential employer.

### **Focus areas for the response based on the role**:
- **Negotiating and drafting** various types of technology agreements, including software, SaaS, data licenses, and professional services agreements.
- **Building business relationships** with internal stakeholders and implementing strategic best practices to limit supply chain risk and exposure.
- **Providing IP-related legal advice**, including IP ownership and licensing, data usage rights, and open-source compliance.
- Assisting with **privacy, information security, contract management**, and other regulatory matters.

Now, please provide a detailed and appealing answer to the following question:

{query}
"""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",  # Using a model with higher token limit
        messages=[
            {"role": "system", "content": "You are a helpful assistant specializing in crafting detailed and appealing responses for job candidates."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,  # Increased token limit for longer responses
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    return response.choices[0].message.content.strip()

# Function to handle the query and display the answer
def handle_query(query):
    with st.spinner("🔍📚 💫"):
        try:
            # Find relevant chunks
            relevant_chunks = find_relevant_chunks(query, all_chunks)
            context = "\n".join(relevant_chunks)
            
            # Generate response
            answer = generate_response(query, context)

            # Formatting the response (better handling for markdown)
            formatted_answer = answer.replace("**", "<b>").replace("\n", "<br>")

            # Adding the necessary HTML tags for bullet points, if they are detected
            formatted_answer = formatted_answer.replace("- ", "<li>").replace("</li><br>", "</li>")

            # Wrapping the answer in a styled div for presentation
            formatted_answer = f'<div class="response-box"><ul>{formatted_answer}</ul></div>'

            # Render the HTML in Streamlit
            st.markdown(formatted_answer, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")



def reset_button_click_state():
    st.session_state.button_clicked = False
    
# Predefined questions
questions = [
    "Can you describe the types of legal contracts Nandini has worked on, and in which industries?",
    "What role does Nandini typically play in cross-functional teams, and how does she collaborate with non-legal stakeholders?",
    "Can you provide examples of how Nandini has handled complex legal negotiations or disputes?",
    "What specific areas of law does Nandini specialize in, and how does her expertise benefit the team?"
]


if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
    
st.markdown('<br>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .stTextInput > div > div > input {
            color: black;
            background-color: #f2f2f2;  /* Softer background for input */
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
    </style>
""", unsafe_allow_html=True)

st.divider()
# Text input for user questions
st.subheader("**You can know more about Nandini, by entering your questions here:**")
user_input = st.text_input("", placeholder="🧙🏻‍♂️: I am an AI-enabled search bar, and can assist you with questions about Nandini")

st.markdown(' 🖋️ Or, **Simply click** these questions below 👇 ', unsafe_allow_html = True)

# Display buttons for predefined questions
cols = st.columns(2)  # Create two columns
for idx, question in enumerate(questions):
    if cols[idx % 2].button(question, key=f'btn{idx}'):
        user_input = question
        st.session_state.button_clicked = True
        handle_query(user_input)

# Handle the user's input if they type a question and press Enter
if user_input and not st.session_state.button_clicked:
    handle_query(user_input)

# Reset the button click state at the end of the session
reset_button_click_state()
st.divider()
# ----------------- skillset ----------------- #


with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        st.markdown('<i class="fa fa-balance-scale" aria-hidden="true"></i> Intellectual Property Law', unsafe_allow_html=True)
    with col2:
        st.markdown('<i class="fa fa-copyright" aria-hidden="true"></i> Copyright Law', unsafe_allow_html=True)
    with col3:
        st.markdown('<i class="fa fa-gavel" aria-hidden="true"></i> Patent Law', unsafe_allow_html=True)
    with col4:
        st.markdown('<i class="fa fa-trademark" aria-hidden="true"></i> Trademarks', unsafe_allow_html=True)
    with col1:
        st.markdown('<i class="fa fa-search" aria-hidden="true"></i> Legal Analysis and Strategy', unsafe_allow_html=True)
    with col2:
        st.markdown('<i class="fa fa-handshake-o" aria-hidden="true"></i> Litigation and Contract Negotiation', unsafe_allow_html=True)
    with col3:
        st.markdown('<i class="fa fa-pencil" aria-hidden="true"></i> Research and Legal Writing', unsafe_allow_html=True)
    with col4:
        st.markdown('<i class="fa fa-users" aria-hidden="true"></i> Cross-functional Collaboration', unsafe_allow_html=True)

    
st.divider()    
# ----------------- timeline ----------------- #
import json

st.subheader('Career Snapshot')

with open('example.json', "r") as f:
    data = json.load(f)

# Reversing the order of events
data['events'].reverse()

with st.spinner(text="Building Timeline"):
    timeline(json.dumps(data), height=500)



st.divider()
# -----------------  endorsement  ----------------- #
st.subheader("👯 Coworker Endorsements")
# Embed an HTML component to display the slideshow
components.html(
f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Styles for the slideshow -->
<style>
    * {{box-sizing: border-box;}}
    .mySlides {{display: none;}}
    img {{vertical-align: middle;}}

    /* Slideshow container */
    .slideshow-container {{
    position: relative;
    margin: auto;
    width: 100%;
    }}

    /* The dots/bullets/indicators */
    .dot {{
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #eaeaea;
    border-radius: 50%;
    display: inline-block;
    transition: background-color 0.6s ease;
    }}

    .active {{
    background-color: #6F6F6F;
    }}

    /* Fading animation */
    .fade {{
    animation-name: fade;
    animation-duration: 1s;
    }}

    @keyframes fade {{
    from {{opacity: .4}} 
    to {{opacity: 1}}
    }}

    /* On smaller screens, decrease text size */
    @media only screen and (max-width: 300px) {{
    .text {{font-size: 11px}}
    }}
    </style>
</head>
<body>
<div class="slideshow-container">
    <div class="mySlides fade">
        <img src="data:image/jpeg;base64,{endorsements['img1']}" style="width:100%">
    </div>

    <div class="mySlides fade">
        <img src="data:image/jpeg;base64,{endorsements['img2']}" style="width:100%">
    </div>

    <div class="mySlides fade">
        <img src="data:image/jpeg;base64,{endorsements['img3']}" style="width:100%">
    </div>
</div>
<br>
<div style="text-align:center">
    <span class="dot"></span> 
    <span class="dot"></span> 
    <span class="dot"></span> 
</div>

<script>
    var slideIndex = 0;
    showSlides();

    function showSlides() {{
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {{
            slides[i].style.display = "none";  
        }}
        slideIndex++;
        if (slideIndex > slides.length) {{slideIndex = 1}}    
        for (i = 0; i < dots.length; i++) {{
            dots[i].className = dots[i].className.replace(" active", "");
        }}
        slides[slideIndex-1].style.display = "block";  
        dots[slideIndex-1].className += " active";
        setTimeout(showSlides, 2500); // Change image every 2.5 seconds
    }}
</script>
</body>
</html> 
""",
height=270,
)

import streamlit as st

with st.sidebar.container():
    st.divider()

    col1, col2, col3 = st.columns(3)
    st.markdown(" ")
    # LinkedIn Icon
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)
    with col1:
        st.markdown(
            """<a href="https://www.linkedin.com/in/nandinicomar/" target="_blank">
                   <i class="fa-brands fa-linkedin fa-beat fa-2x" style="color: #ff0000;"></i>
               </a>""",
            unsafe_allow_html=True
        )

    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)
    # Email Icon
    with col2:
        st.markdown(
            """<a href="mailto:comarnan@gmail.com">
                   <i class="fa-regular fa-envelope fa-beat fa-2x" style="color: #000000;"></i>
               </a>""",
            unsafe_allow_html=True
        )

    # Phone Icon
    with col3:
        st.markdown(
            """<a href="tel:+1.201.620.1544">
                   <i class="fa-solid fa-phone fa-beat fa-2x" style="color: #fff700;"></i>
               </a>""",
            unsafe_allow_html=True
        )

