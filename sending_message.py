import speech_recognition as sr
from systemOperations import speak
import keyboard
import pywhatkit as kit
import smtplib
import time


def text_for_message():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell your message: ")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    
def phone_for_message():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell your phone number: ")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    
def send_whatsapp_message():
    phoneno = "+91" + phone_for_message()
    text = text_for_message()
    kit.sendwhatmsg_instantly(phoneno,text)
    speak("please wait for a while for your poor network connection...")
    time.sleep(5)
    keyboard.press('enter')
    speak("message sent successfully...")

def email_message():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell me the message: ")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""

def name_of_person():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell me the name of the person: ")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
def send_email(email,text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('parthibkarak61@gmail.com', 'xbgvqbwlsdvaztyy')
    server.sendmail('parthibkarak61@gmail.com', email, f'{text}')   
    server.quit()
    