import streamlit as st
from processCommand import messages
from shared import speak
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Function to listen to speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        print("Network error. Please check your internet connection.")
        return ""

# Function to interact with the assistant
def interact_with_assistant():
    conversation_history = []  # Initialize conversation history
    history_key = "conversation_history"  # Use a fixed key for conversation history
    while True:
        # Listen for command
        command = listen()
        
        if command in ["melody", "ok melody", "hi melody"]:
            response = "Hi, I am Melody! How can I help you?"
            conversation_history.append(f"Melody: {response}")
            speak(response)
            
            while True:
                # Listen for user input
                command = listen()
                if command in ["exit", "quit", "goodbye"]:
                    response = "Goodbye!"
                    conversation_history.append(f"Melody: {response}")
                    speak(response)
                    break
                elif command:
                    # Call the messages function to process the command
                    assistant_response = messages(command)
                    response = f"Melody: {assistant_response}"
                    conversation_history.append(response)
                    speak(response)

        elif command in ["exit", "quit", "goodbye"]:
            response = "Goodbye!"
            conversation_history.append(f"Melody: {response}")
            speak(response)
            break
            
        # Display conversation history in a text area with a unique key
        conversation_text = "\n".join(conversation_history)
        st.text_area("Conversation History", conversation_text, height=300, key=history_key)

# Streamlit web app
def main():
    st.title("Voice Assistant: Melody")
    
    # Add a button to start the assistant
    if st.button("Start Melody"):
        st.write("Assistant is listening...")
        interact_with_assistant()
    
if __name__ == "__main__":
    main()
