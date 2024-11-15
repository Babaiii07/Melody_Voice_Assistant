import streamlit as st
from processCommand import messages
from shared import speak
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Function to listen to speech input
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        st.warning("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        st.error("Network error. Please check your internet connection.")
        return ""

# Function to interact with the assistant
def interact_with_assistant():
    if "conversation_history" not in st.session_state:
        st.session_state["conversation_history"] = []  # Initialize session-based conversation history

    while st.session_state.get("is_running", False):
        # Listen for command
        command = listen()

        if command in ["melody", "ok melody", "hi melody"]:
            response = "Hi, I am Melody! How can I help you?"
            st.session_state["conversation_history"].append(f"User: {command}")  # Add user input
            st.session_state["conversation_history"].append(f"Melody: {response}")  # Add assistant response
            speak(response)
            
            while st.session_state.get("is_running", False):
                # Listen for user input
                command = listen()
                if command in ["exit", "quit", "goodbye"]:
                    response = "Goodbye!"
                    st.session_state["conversation_history"].append(f"User: {command}")  # Add user input
                    st.session_state["conversation_history"].append(f"Melody: {response}")  # Add assistant response
                    speak(response)
                    st.session_state["is_running"] = False
                    break
                elif command:
                    # Call the messages function to process the command
                    assistant_response = messages(command)
                    if assistant_response:
                        response = f"Melody: {assistant_response}"
                        st.session_state["conversation_history"].append(f"User: {command}")  # Add user input
                        st.session_state["conversation_history"].append(response)  # Add assistant response
                        speak(response)

                # Update conversation history in real-time
                st.session_state["conversation_text"] = "\n".join(st.session_state["conversation_history"])

                # Display entire conversation on the page
                st.write(f"### Conversation History:")
                for line in st.session_state["conversation_history"]:
                    st.write(line)

# Streamlit web app
def main():
    st.title("Voice Assistant: Melody")

    # Start/Stop Assistant
    if "is_running" not in st.session_state:
        st.session_state["is_running"] = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Melody"):
            st.session_state["is_running"] = True
            st.write("Assistant is listening...")
            interact_with_assistant()
    
    with col2:
        if st.button("Stop Melody"):
            st.session_state["is_running"] = False
            st.write("Assistant stopped.")

    # Display conversation history
    if "conversation_text" in st.session_state:
        st.write(f"### Full Conversation History:")
        for line in st.session_state["conversation_history"]:
            st.write(line)

if __name__ == "__main__":
    main()