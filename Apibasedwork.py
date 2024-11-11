import requests
from systemOperations import speak
import speech_recognition as sr
from bs4 import BeautifulSoup
import subprocess
import streamlit as st

API_KEY = '56163bbceae345788e96f34b6b1e62d3' #news api
def aiProcess(prompt):
    command = ["ollama", "run", "llama3.2"]
    prompt1 = prompt + "in short"
    st.write("please wait few minutes ..your prompt is generating")
    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        output, error = process.communicate(input=prompt1)
        if output:
            return output.strip()
        if error:
            return f"Error occurred: {error.strip()}"
    
    except Exception as e:
        return f"An exception occurred: {str(e)}"
    
def listen_for_voiceChat():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""

def take_name_city():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("please tell me the city name: ")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    
def weather_report():
    city = take_name_city()
    weather_api = "14823a5d80b64090ba5124120241409"
    base_url = 'http://api.weatherapi.com/v1/current.json' 
    url = f'{base_url}?key={weather_api}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name'] 
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text'] 
        
        print(f"Weather in {location}:")
        speak(f"Weather in {location}:")
        
        print(f"Temperature: {temp_c}°C") 
        speak(f"Temperature: {temp_c}°C")
        
        print(f"Condition: {condition}") 
        speak(f"Condition: {condition}")

def take_topic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("what would you like to search in news topic")
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    
def tell_news():
    topic = take_topic()
    get_news(topic)
def get_news(query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        for idx, article in enumerate(articles[:3], 1):
            article_content = scrape_article(article['url'])
            if article_content:
                print(f"\nFull Article {idx}:\n")
                speak(article_content)
                print(f"{'-'*80}")
            else:
                speak(f"\nCouldn't fetch the full article content for article {idx}.\n")
    else:
        print("Error:", response.status_code)
    

def scrape_article(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')
        content = "\n".join([para.get_text() for para in paragraphs])

        return content if content else None
    except Exception as e:
        print(f"Error scraping article: {e}")
        return None
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        print("Recognizing...")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return "" 

def genarate_image():
    speak("tell me the topic")
    command = take_command()
    command2 = take_command()
    if command2 :
        newcommand = command + command2
        
    pass

