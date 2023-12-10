import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from constant import *
from PIL import Image
import openai
from langchain.chat_models import ChatOpenAI
import base64
from llama_index import Prompt


st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')

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
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']
with col1:
    gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])     
    
# ----------------- Llama ----------------- #
openai.api_key = st.secrets["OPENAI_API_KEY"]

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    '''Given this information, please answer the question and follow these guidelines when answering - 
        1. Each answer should be taste fully written in a bullet point format 
        2. Add new lines 
        3. Answer should contains emojis
        4. Make the Answer short
        5. VERY IMPORTANT: You are replying to a potential hiring manager or recruitor, so make sure you word the answer in a way that it appeals them - 
        6. Use Markdown formats to make sure you highlight and underline important parts of the reply
        7. When ever you answer the question, and it contains many parts, Make a header for the part, and list your answer below it. For example - For question - Can you elaborate on Nandini's specialization in intellectual property law and how she has applied it in her past roles?
        
        You will list part 1 -  Can you elaborate on Nandini's specialization in intellectual property law
        and part 2 - how she has applied it in her past roles
        
        and add answer below these
        {query_str}\n'''
)
qa_template = Prompt(template)

query_engine = index.as_query_engine(text_qa_template=qa_template)

# Function to handle the query and display the answer
# Function to handle the query and display the answer
def handle_query(query):
    with st.spinner('🔍 Analyzing Nandini’s expertise... 📚 Please hold on a moment! 💫'):
        try:
            answer = query_engine.query(query).response

            # Splitting the response into parts and bolding text between '**'
            parts = answer.split('**')
            formatted_answer = ''
            for i, part in enumerate(parts):
                if i % 2 == 1:  # This is the text that should be bold
                    formatted_answer += f'<b>{part}</b>'
                else:
                    formatted_answer += part

            # Replace bullet points with HTML list items
            formatted_answer = formatted_answer.replace("- ", "<li>")
            formatted_answer = formatted_answer.replace("\n", "</li>")

            # Wrap the response in a div with a class for styling
            formatted_answer = f'<div class="response-box"><ul>{formatted_answer}</ul></div>'

            st.markdown(formatted_answer, unsafe_allow_html=True)
        except Exception as e:
            st.error("An error occurred: " + str(e))


# Predefined questions
questions = [
    "What are Nandini's key achievements in her legal career?",
    "Can you elaborate on Nandini's specialization in intellectual property law and how she has applied it in her past roles?",
    "What unique skills does Nandini bring to a legal team, and how have these contributed to her previous workplaces?",
    "How has Nandini demonstrated professional growth throughout her career, and what are her long-term career aspirations?"
]

st.markdown("<h4 style='text-align: Left; color: White;'>I am an AI-enabled search bar, and can assist you with questions about Nandini</h4>", unsafe_allow_html=True)


# Display buttons for predefined questions side by side
cols = st.columns(2)  # Create two columns
for idx, question in enumerate(questions):
    if cols[idx % 2].button(question, key=f'btn{idx}'):
        user_input = question
        handle_query(user_input)
        
# Text input for user questions
user_input = st.text_input("Enter your question here: ", placeholder="For example: Provide me bullet points of Nandini’s experience in IP Law")

# Handle the user's input if they type a question and press Enter
if user_input and not st.session_state.get('button_clicked', False):
    handle_query(user_input)



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

    
    
# ----------------- timeline ----------------- #
st.subheader('Career snapshot')


    
with st.spinner(text="Building line"):
    with open('example.json', "r") as f:
        data = f.read()
        timeline(data, height=500)


# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2,col3 = st.columns([0.475, 0.475, 0.05])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("👄 Coworker Endorsements")
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

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
