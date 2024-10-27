import subprocess
import pyttsx3
import os
import datetime
import speech_recognition as sr
import pyautogui 
import time
import cpuinfo
import psutil
import platform

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def open_chrome():
    subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])

def open_calculator():
    subprocess.Popen(["calc.exe"])

def open_word():
    subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])

def open_powerpoint():
    subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"])

def lock_system():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def shutdown_system():
    os.system("shutdown /s /t 1")

def clear_recycle_bin():
    os.system("PowerShell.exe -NoProfile -Command \"Clear-RecycleBin -Force\"")

def restart_system():
    os.system("shutdown /r /t 1")

def sleep_system():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def open_notepad():
    subprocess.Popen(["notepad.exe"])
    speak("notepad opened...")
    time.sleep(2)
    speak("please say something that i will noted down")
    note = take_voice_note()
    pyautogui.write(note)
    pyautogui.press("enter")
    speak("Note saved...")

def take_voice_note():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        note = recognizer.recognize_google(audio)
        with open("/notes/voice_notes.txt", "a") as file:
            file.write(note + "\n")
        speak("Note saved: " + note)
    except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")

def open_settings():
    speak("opening settings...")
    os.startfile('C:\\Windows\\System32\\control.exe "sysdm.cpl"')

def open_file_explorer():
    speak("opening file explorer...")
    os.startfile('C:\\Windows\\explorer.exe')
def open_paint():
    speak("opening paint...")
    os.startfile('C:\\Windows\\System32\\mspaint.exe')

def get_current_date():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    return date


def pc_configuration():
    speak("Here is your PC configuration...")
    cpu_info = cpuinfo.get_cpu_info()
    speak(f"CPU: {cpu_info['brand']} {cpu_info['arch']}")
    speak(f"RAM: {psutil.virtual_memory().total / (1024 * 1024)} MB")
    speak(f"Operating System: {platform.system()} {platform.release()}")
    speak(f"Python Version: {platform.python_version()}")

def set_alarm():
    speak("Setting an alarm...")
    time.sleep(1)
    speak("Please say the alarm time in A.M and P.M format")
    alarm_time = time_alarm_listen()
    
    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M").time()
        speak(f"Setting alarm at {alarm_time.strftime('%I:%M %p')}")
        
        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= alarm_time:
                speak("Alarm! Time's up!")
                break
            time.sleep(1)
    except ValueError:
        speak("Sorry, I couldn't understand the alarm time. Please try again.")
    except Exception as e:
        speak("Sorry, there was an error setting the alarm.")
        print(f"Error: {e}")

def time_alarm_listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for alarm time...")
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        return text

def open_onenote():
    speak("opening oneNote...")
    os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')






