import webbrowser
import os
import pyjokes
import pywhatkit as kit
import speech_recognition as sr
from shared import speak

def open_google():
    webbrowser.open('https://www.google.com/')
def open_facebook():
    webbrowser.open('https://www.facebook.com/')
def open_youtube():
    webbrowser.open('https://www.youtube.com/')

def open_linkedin():
    webbrowser.open('https://www.linkedin.com/')

def open_github():
    webbrowser.open('https://www.github.com/')

def open_wikipedia():
    webbrowser.open('https://www.wikipedia.org/')

def open_whatsapp():
    webbrowser.open('https://web.whatsapp.com/')

def open_instagram():
    webbrowser.open('https://www.instagram.com/')

def open_discord():
    webbrowser.open('https://discord.com/')

def open_edge():
    os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

def open_twitter():
    webbrowser.open('https://www.twitter.com/')

def open_spotify():
    webbrowser.open('https://open.spotify.com/')

def open_reddit():
    webbrowser.open('https://www.reddit.com/')

def open_netflix():
    webbrowser.open('https://www.netflix.com/')

def open_tiktok():
    webbrowser.open('https://www.tiktok.com/')
def open_amazon():
    webbrowser.open('https://www.amazon.com/')
def open_flipkart():
    webbrowser.open('https://www.flipkart.com/')

def play_jokes():
    joke = pyjokes.get_joke('en', 'neutral')
    speak(joke)

def play_song():
    song_name = listen_songName()
    if song_name :
        kit.playonyt(song_name)
        speak(f'Playing {song_name}...')

def listen_songName():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell me the song name..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    
def open_google_maps():
    webbrowser.open('https://www.google.com/maps/')

def open_yahoo():
    webbrowser.open('https://www.yahoo.com/')

def open_stackoverflow():
    webbrowser.open('https://stackoverflow.com/')

def open_gmail():
    webbrowser.open('https://mail.google.com/')

def open_drive():
    webbrowser.open('https://drive.google.com/')

def open_calendar():
    webbrowser.open('https://calendar.google.com/')
def open_google_classroom():
    webbrowser.open('https://classroom.google.com/')

def open_ebay():
    webbrowser.open('https://www.ebay.com/')
def open_pinterest():
    webbrowser.open('https://www.pinterest.com/')

def open_tumblr():
    webbrowser.open('https://www.tumblr.com/')
