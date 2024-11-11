from systemOperations import open_calculator,open_chrome,open_file_explorer,open_notepad,open_paint,open_powerpoint,open_settings,open_word,get_current_time,get_current_date,shutdown_system,set_alarm,sleep_system,pc_configuration,restart_system,clear_recycle_bin,lock_system,open_onenote
from websites import open_google,open_facebook,open_youtube,open_linkedin,open_github,open_wikipedia,open_whatsapp,open_instagram,open_discord,open_edge,open_twitter,open_spotify,open_reddit,open_netflix,open_tiktok,open_google_maps,open_yahoo,open_stackoverflow,open_gmail,open_drive,open_calendar,open_google_classroom,play_jokes,play_song,open_amazon,open_flipkart,open_ebay,open_pinterest,open_tumblr
from sending_message import send_whatsapp_message,email_message,send_email
from picture import take_screenshot,take_selfie
from Apibasedwork import weather_report,tell_news,genarate_image,aiProcess,listen_for_voiceChat
from shared import speak
import spacy
import wikipedia
import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

nlp = spacy.load("en_core_web_sm")

def messages(text):
    command = text.lower()
    if "calculator" in command:
        open_calculator()
        speak("calculator opened...")
        print("calculator opened...")
    elif "chrome" in command:
        open_chrome()
        speak("chrome opened...")
        print("chrome opened...")

    elif "file explorer" in command:
        open_file_explorer()
        speak("file explorer opened...")
        print("file explorer opened...")

    elif "notepad" in command or "take a note" in command:
        open_notepad()
        speak("notepad opened...")
        print("notepad opened...")
    elif "paint" in command:
        open_paint()
        speak("paint opened...")
        print("paint opened...")
    elif "powerpoint" in command:
        open_powerpoint()
        speak("powerpoint opened...")
        print("powerpoint opened...")
    elif "settings" in command:
        open_settings()
        speak("settings opened...")
        print("settings opened...")
    elif "word" in command:
        open_word()
        speak("word opened...")
        print("word opened...")
    elif "time" in command:
        current_time = get_current_time()
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = get_current_date()
        speak(f"The current date is {current_date}")
    elif "shutdown" in command:
        shutdown_system()
        speak("System is shutting down...")
        print("System is shutting down...")
    elif "alarm" in command:
        set_alarm()
        speak("Alarm set...")
        print("Alarm set...")
    elif "sleep" in command:
        sleep_system()
        speak("System is sleeping...")
        print("System is sleeping...")
    elif "pc configuration" in command:
        pc_configuration()
        speak("PC configuration is displayed...")
        print("PC configuration is displayed...")
    elif "restart" in command:
        restart_system()
        speak("System is restarting...")
        print("System is restarting...")
    elif "recycle bin" in command:
        clear_recycle_bin()
        speak("Recycle bin cleared...")
        print("Recycle bin cleared...")
    elif "lock" in command:
        lock_system()
        speak("System is locked...")
        print("System is locked...")
    elif "onenote" in command:
        open_onenote()
        speak("OneNote opened...")
        print("OneNote opened...")
    elif "google" in command:
        open_google()
        speak("Google search opened...")
        print("Google search opened...")
    elif "facebook" in command:
        open_facebook()
        speak("Facebook opened...")
        print("Facebook opened...")
    elif "youtube" in command:
        open_youtube()
        speak("YouTube opened...")
        print("YouTube opened...")
    elif "linkedin" in command:
        open_linkedin()
        speak("LinkedIn opened...")
        print("LinkedIn opened...")
    elif "github" in command:
        open_github()
        speak("GitHub opened...")
        print("GitHub opened...")
    elif "wikipedia" in command:
        open_wikipedia()
        speak("Wikipedia opened...")
        print("Wikipedia opened...")
    elif "whatsapp" in command:
        if "send whatsapp message" in command or "whatsapp message" in command:
            send_whatsapp_message()
        elif "open" in command or "whatsapp" in command:
            open_whatsapp()
            speak("Whatsapp opened...")
            print("Whatsapp opened...")
        else :
            airesponse = aiProcess(command)
            print(f"airesponse:{airesponse}")
            speak(airesponse)
    elif "instagram" in command:
        open_instagram()
        speak("Instagram opened...")
        print("Instagram opened...")
    elif "discord" in command:
        open_discord()
        speak("Discord opened...")
        print("Discord opened...")
    elif "edge" in command:
        open_edge()
        speak("Edge opened...")
        print("Edge opened...")
    elif "twitter" in command:
        open_twitter()
        speak("Twitter opened...")
        print("Twitter opened...")
    elif "spotify" in command:
        open_spotify()
        speak("Spotify opened...")
        print("Spotify opened...")
    elif "reddit" in command:
        open_reddit()
        speak("Reddit opened...")
        print("Reddit opened...")
    elif "netflix" in command:
        open_netflix()
        speak("Netflix opened...")
        print("Netflix opened...")
    elif "tiktok" in command:
        open_tiktok()
        speak("TikTok opened...")
        print("TikTok opened...")
    elif "google maps" in command:
        open_google_maps()
        speak("Google Maps opened...")
        print("Google Maps opened...")
    elif "yahoo" in command:
        open_yahoo()
        speak("Yahoo opened...")
        print("Yahoo opened...")
    elif "stack overflow" in command:
        open_stackoverflow()
        speak("StackOverflow opened...")
        print("StackOverflow opened...")
    elif "gmail" in command:
        open_gmail()
        speak("Gmail opened...")
    elif "drive" in command or "google drive" in command:
        open_drive()
        speak("Google Drive opened...")
        print("Google Drive opened...")
    elif "calendar" in command:
        open_calendar()
        speak("Google Calendar opened...")
        print("Google Calendar opened...")
    elif "google classroom" in command or "classroom" in command:
        open_google_classroom()
        speak("Google Classroom opened...")
        print("Google Classroom opened...")
    elif "jokes" in command or "joke" in command:
        play_jokes()
        speak("Joke played...")
        print("Joke played...")
    elif "song" in command or "song" in command or "music" in command or "play" in command:
        play_song()
        speak("Song played...")
        print("Song played...")
    elif "amazon" in command:
        open_amazon()
        speak("Amazon opened...")
        print("Amazon opened...")
    elif "flipkart" in command:
        open_flipkart()
        speak("Flipkart opened...")
        print("Flipkart opened...")
    elif "ebay" in command:
        open_ebay()
        speak("eBay opened...")
        print("eBay opened...")
    elif "pinterest" in command:
        open_pinterest()
        speak("Pinterest opened...")
        print("Pinterest opened...")
    elif "tumblr" in command:
        open_tumblr()
        speak("Tumblr opened...")
        print("tumblr opened...")
    elif "selfie" in command or "photo"in command or "snap" in command:
        take_selfie()
        speak("Selfie taken...")
        print("Selfie taken...")
    elif "screenshot" in command:
        take_screenshot()
        speak("Screenshot taken...")
        print("Screenshot taken...")
    elif "weather" in command:
        weather_report()
    elif "news" in command:
        tell_news()
    elif command.startswith("generate an image of ") or command.startswith("create an image of") or command.startswith("image of"):
        genarate_image()
        speak("Image generated...")
        print("Image generated...")
    elif command.startswith("send a email to") or command.startswith("can you send a email to") or command.startswith("can you please send a email to"):
        recipents = command.split()
        if "to" in recipents:
            index_of_to = recipents.index("to")
            if index_of_to + 1 < len(recipents):
                next_word = recipents[index_of_to + 1]
                new_recipents = next_word
                message = email_message()
                send_email(new_recipents, message)
                speak("Email sent...")
                print("Email sent...")

    elif "lets" in command or "chat" in command:
        os.environ["AI21_API_KEY"] = "qjppcwCa162aacuFa5YzBu1aNPZ7ifus"
        client = AI21Client()
        system_message = ChatMessage(
            role="system",
            content="Your name is Melody. You are a virtual voice assistant. You can chat with the user as a friend and help them with your best."
        )
        while True:
            newCommand = listen_for_voiceChat()
            user_message = ChatMessage(
                role="user",
                content=newCommand
            )
            
            response = client.chat.completions.create(
                model="jamba-instruct-preview",  
                messages=[system_message, user_message],
                temperature=0.8,
                max_tokens=200 
            )
            
            content = response.choices[0].message.content
            speak(content)
            print(content)

    elif command.startswith("tell me about"):
        subject = command.split()
        if "about" in subject:
            index_of_about = subject.index("about")
            if index_of_about + 1 < len(subject):
                next_word = " ".join(subject[index_of_about + 1:])
                search_results = wikipedia.search(next_word, results=5)

                if search_results:
                    page_title = search_results[0]
                    try:
                        page_summary = wikipedia.summary(page_title, sentences=2)
                        print(f"According to Wikipedia, {page_summary}")
                        speak(f"According to Wikipedia, {page_summary}")
                    except wikipedia.exceptions.DisambiguationError as e:
                        speak(f"There are multiple entries for {next_word}. Can you be more specific?")
                        print(f"There are multiple entries for {next_word}. Can you be more specific?")
                    except wikipedia.exceptions.PageError:
                        speak(f"Sorry, I couldn't find a page for {next_word}.")
                        print(f"Sorry, I couldn't find a page for {next_word}.")
                else:
                    speak(f"Sorry, I couldn't find any results for {next_word}.")
                    print(f"Sorry, I couldn't find any results for {next_word}.")

    else :
        airesponse = aiProcess(command)
        print(f"aiResponse:{airesponse}")
        speak(airesponse)

                
        


        

        



        

        