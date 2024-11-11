from processCommand import messages
from shared import speak
import speech_recognition as sr

def listen():
    r = sr.Recognizer()
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

if __name__ == "__main__":
    while True:
        command = listen()
        if command in ["melody", "ok melody", "hi melody"]:
            print("Hi, I am Melody! How can I help you?")
            speak("Hi, I am Melody! How can I help you?")
            while True:
                command = listen()
                if command in ["exit", "quit", "goodbye"]:
                    print("Goodbye!")
                    speak("Goodbye!")
                    break
                elif command:
                    messages(command)
        elif command in ["exit", "quit", "goodbye"]:
            print("Goodbye!")
            speak("Goodbye!")
            break
