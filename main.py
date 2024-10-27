import streamlit as st
import speech_recognition as sr
from shared import speak
from processCommand import messages 
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("NLP model not found. Run `python -m spacy download en_core_web_sm` to install.")
st.set_page_config(page_title="Melody Voice Assistant", layout="centered")

def set_page_style():
    st.markdown("""
        <style>
        .pulse-circle {
            width: 15vw; height: 15vw;
            min-width: 100px; min-height: 100px;
            border-radius: 50%;
            background: rgba(255, 64, 129, 0.8);
            position: relative; margin: 0 auto;
            animation: pulse 1.5s infinite;
            box-shadow: 0 0 20px rgba(255, 64, 129, 0.6);
        }
        @keyframes pulse {
            0% { transform: scale(0.9); opacity: 0.7; }
            70% { transform: scale(1); opacity: 0.2; }
            100% { transform: scale(0.9); opacity: 0.7; }
        }
        </style>
    """, unsafe_allow_html=True)
def about_page():
    st.title("About Melody Voice Assistant")
    st.write("""
        **Melody** is a virtual voice assistant designed for intuitive, hands-free device interaction. It can answer questions, 
        search for information, tell jokes, and more.
    """)

    contributors = [
        {"name": "Parthib Karak", "Role": "Role : Backend", "github": "https://github.com/Parthibkarak71",
         "image": "https://media.licdn.com/dms/image/v2/D4D03AQHA0kMEuC5kbA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1691222092711?e=2147483647&v=beta&t=bIsHgg6ugKpadGZiQsvjSKOM9QdWyVKGocF3Kf1mlhA"},
        {"name": "Agnik Bishi", "Role": "Role : System Designer, Model Architecture Design,Documentation Paper", "github": "https://github.com/JISHUBISHI",
         "image": "https://media.licdn.com/dms/image/D5603AQFULGfEVGKuXQ/profile-displayphoto-shrink_200_200/0/1706333608891?e=2147483647&v=beta&t=1398vJfLcfUuwtibm97Oaq6uI5hGtPCWsA2jDv7gWKY"},
        {"name": "Roki Ghosh", "Role": "Frontend, Backend", "github": "https://github.com/ROKIGHOSH",
         "image": "https://media.licdn.com/dms/image/v2/D4D03AQH2DQfe024IbA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1730008620727?e=1735776000&v=beta&t=49QczQ7MUjsjiiMLFt8PmE498u2MRMYBMzH7gOEDWxw"}
    ]

    st.markdown("""
        <style>
            .contributor-container { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
            .contributor-img { width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #007BFF; }
            .github-logo { width: 24px; height: 24px; margin-left: 10px; }
        </style>
    """, unsafe_allow_html=True)

    for contributor in contributors:
        st.markdown(f"""
        <div class="contributor-container">
            <img src="{contributor['image']}" class="contributor-img" alt="Contributor Image">
            <div>
                <p><strong>{contributor['name']}</strong><br>
                <em>{contributor['Role']}</em></p>
                <a href="{contributor['github']}" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" class="github-logo" alt="GitHub Logo">
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            st.session_state['last_command'] = command
            st.session_state['history'].append(f"User: {command}")
            return command
        except sr.UnknownValueError:
            st.write("Sorry, I didn't catch that.")
        except sr.RequestError:
            st.write("API error; check your internet connection.")
def process_command(command):
    response = messages(command)
    speak(response)
    st.session_state['history'].append(f"Melody: {response}")
def melody_assistant():
    set_page_style()
    st.title("Melody Voice Assistant")
    st.markdown("""<div class="pulse-circle"></div>""", unsafe_allow_html=True)

    if 'history' not in st.session_state:
        st.session_state['history'] = []
    
    if 'listening' not in st.session_state:
        st.session_state['listening'] = False
    if st.button("Listen") and not st.session_state['listening']:
        st.session_state['listening'] = True 
        command = listen_command()
        if command:
            if command.lower() in ["melody", "hi melody", "ok melody"]:
                st.write("Hi! I'm Melody, your virtual voice assistant.")
                speak("Hi! I'm Melody, your virtual voice assistant.")
                while True:
                    command = listen_command() 
                    if command: 
                        process_command(command)
            else:
                process_command(command)
        st.session_state['listening'] = False 

    if st.button("Stop Assistant"):
        speak("Assistant stopped.")
    
    st.write("**Command History:**")
    for entry in st.session_state['history']:
        st.write(entry)
def documentation_page():
    st.title("Melody Voice Assistant Documentation")
    st.write("""
        This page provides an overview of interacting with Melody, including available commands, usage tips, and troubleshooting.
        ### Available Commands
        - **General Information**: "What's the capital of France?"
        - **Jokes**: "Tell me a joke."
        - **Search**: "Find information on artificial intelligence."
    """)
page = st.sidebar.radio("Navigate", ["Assistant", "About", "Documentation"])
if page == "Assistant":
    melody_assistant()
elif page == "About":
    about_page()
elif page == "Documentation":
    documentation_page()
