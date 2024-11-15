from deep_translator import GoogleTranslator
from processCommand import messages
from shared import speak
import speech_recognition as sr

def translate_to_english(text):
    """
    This function translates input text to English using deep-translator (Google Translate).
    """
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

def command(text):
    input_text = text.lower()
    translated_text = translate_to_english(input_text)
    return translated_text

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  
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

def main():
    while True:
        command_input = listen()

        if command_input in ["melody", "ok melody", "hi melody"]:
            print("Hi, I am Melody! How can I help you?")
            speak("Hi, I am Melody! How can I help you?")
            
            while True:
                command_input = listen()
                if command_input in ["exit", "quit", "goodbye"]:
                    print("Goodbye!")
                    speak("Goodbye!")
                    break
                elif command_input:
                    translated_command = command(command_input)
                    messages(translated_command)

        elif command_input in ["exit", "quit", "goodbye"]:
            print("Goodbye!")
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
