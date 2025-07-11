import pyttsx3
import datetime
import webbrowser
import speech_recognition as sr
import os
import openai
from config import apikey
import wikipedia
import pyjokes
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import matplotlib.pyplot as plt
from pygame import mixer
import requests
import json
import pyautogui

from plyer import notification


# OpenAI function for AI response
def ai(prompt):
    openai.api_key = apikey

    # Create a chat completion
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text = response["choices"][0]["message"]["content"]
    
    # Save the response to a file
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    filename = f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"
    with open(filename, "w") as f:
        f.write(text)
    
    return text

# setting up engine and its properties
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = r.listen(source)  # Listen to the user's input

    try:
        print("Recognizing...")
        password_spoken = r.recognize_google(audio)  # Use Google's API to convert speech to text
        print(f"User said: {password_spoken}")
        return password_spoken
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("There seems to be an issue with the speech recognition service.")
        return ""

def speak(audio):
    """Speak function to give output in voice format"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Function to wish the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("Sahil, how can I help you?")

def takeCommand():
    """Takes voice command from the user and performs specific actions"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize speech
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        # Opening websites based on voice command
        sites = [
            ["youtube", "https://youtube.com"],
            ["ai", "https://chatgpt.com"],
            ["google", "https://google.com"],
            ["tuf", "https://takeuforward.org/"],
            ["wikipedia", "https://www.wikipedia.org/"],
            ["email","https://mail.google.com/mail/u/0/#inbox"],
            ["linkedin","https://www.linkedin.com/in/sahil-koshti-726523289/"]
        ]

        for site in sites:
            if f"open {site[0]}" in query.lower():
                speak(f"Opening {site[0]} ...")
                webbrowser.open(site[1])

        # Opening system files
        if "open searching" in query.lower():
            speak("Opening searching...")
            fp = "C:\PLACEMENTS\DSA"  # Escape backslashes in the path
            os.startfile(fp)

        if "open apache" in query.lower():
            speak("Opening Apache...")
            fp1 = "C:\Program Files\Apache Software Foundation"
            os.startfile(fp1)

        # Time query
        if "the time" in query.lower():
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        # Open Chrome
        if "open chrome" in query.lower():
            speak("Opening Chrome")
            os.system("start chrome")

        # Open VLC Media Player
        if "open media player" in query.lower():
            speak("Opening VLC Media Player")
            os.system("start vlc")

        # If user requests AI assistance
        if "using artificial intelligence" in query.lower():
            response = ai(query)
            speak(response)

        if "tell me a joke" in query.lower():
             joke = pyjokes.get_joke()
             speak(joke)

        if "paint" in query.lower():
             window = tk.Tk()
             window.title("Jarvis AI")
             label = tk.Label(window, text="Welcome to Jarvis AI!")
             label.pack()
             window.mainloop()

        if "gui" in query.lower():
            app = QApplication([])
            window = QWidget()
            window.setWindowTitle('Jarvis AI Assistant')
            label = QLabel('Welcome to Jarvis AI!', parent=window)
            label.move(60, 15)
            window.setGeometry(100, 100, 280, 80)
            window.show()
            app.exec_()

        if "ds" in query.lower():
             x = [1, 2, 3, 4, 5]
             y = [2, 3, 5, 7, 11]
             plt.plot(x, y)
             plt.title("Prime Number Plot")
             plt.xlabel("x-axis")
             plt.ylabel("y-axis")
             plt.show()

        if "play" in query:
            pyautogui.press("k")
        
        if "mute" in query:
            pyautogui.press("m")

        if "minimize" in query:
            pyautogui.press("i")
        
        if "up" in query:
            from keyboard import volumeup
            speak("Turning up volume")
            volumeup()

        if "down" in query:
            from keyboard import volumedown
            speak("Turning down volume")
            volumedown()

        if "calculate" in query.lower():
            from calculator import wolframalpha
            from calculator import calculate
            query=query.replace("Jarvis","")
            query=query.replace("calculate","")
            calculate(query)
        
        if "Whatsapp" in query.lower():
            update=int((datetime.now()+timedelta(minutes=2)).strftime("%M"))
            strTime=int(datetime.now().strftime("%H"))

            def sendmessage():
                speak("Who do you want to send message")
                a = int(input('''Person 1 - 1
                Person 2 - 2'''))
                try:
                    
                    if a == 1:
                        
                        speak("Whats the message")
                        message = str(input("Enter the message- "))
                        pywhatkit.sendwhatmsg("+919974745061",message,time_hour=strTime,time_min=update)
                    elif a==2:
                        message = str(input("Enter the message- "))
                        pywhatkit.sendwhatmsg("+919974745061",message,time_hour=strTime,time_min=update)
                except:
                    speak("Something Went Wrong")

                
        
    

        return query

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return None

def search_wikipedia(query):
    """Search Wikipedia and return the first sentence of the summary"""
    speak(f"Searching Wikipedia... {query}")
    try:
        # Search Wikipedia for the query and get a summary (first 1-2 sentences)
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"There are multiple results for {query}. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find anything on Wikipedia for your query.")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")
        print(e)



def latestnews(query):
  

    # Define sites as a list of lists [category, URL]
    sites = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=26faa476d12a484c8543d0e94d542ce0",
        "tech": "https://newsapi.org/v2/everything?q=tesla&from=2024-08-19&sortBy=publishedAt&apiKey=26faa476d12a484c8543d0e94d542ce0"
    }
    found = False
    
    for site in sites:
        if f"open {site[0]}" in query.lower():
            speak(f"Fetching {site[0]} news...")
            
            # Make the API request
            response = requests.get(site[1])
            news = response.json()

            if "articles" in news:
                arts = news["articles"]
                
                # Loop through each article in the 'articles' list
                for article in arts:
                    # Safely get the title and URL of each article
                    title = article.get("title", "No title available")
                    news_url = article.get("url", "No URL available")
                    
                    # Print and speak the title and provide the URL
                    print(title)
                    speak(title)
                    print(f"For more info, visit: {news_url}")
            else:
                speak(f"No articles found in the response for {site[0]}.")
                speak(f"Response content: {news}")

            found = True
            break  # Exit the loop since we found a match
    
    # If no matching category was found
    if not found:
        speak("No matching news category found.")


def SecduleMyDay(query):
    tasks=[]
    speak("Do You want to clear your old tasks Say Yes or No")
    query=recognize_speech()
    if "yes" in query:
        file=open("tasks.txt","w")
        file.write(f"")
        file.close()

        no_tasks=int(input("Enter the number of tasks"))
        i=0
        for i in range(no_tasks):
            tasks.append(input("Enter the task"))
            file=open("tasks.txt","a")
            file.write(f"{i}.{tasks.i}\n")
            file.close()

    elif "no" in query:
        no_tasks=int(input("Enter the number of tasks"))
        i=0
        for i in range(no_tasks):
            tasks.append(input("Enter the task"))
            file=open("tasks.txt","a")
            file.write(f"{i}.{tasks.i}\n")
            file.close()
    elif "show tasks" in query.lower():
        file=open("tasks.txt","r")
        content=file.read()
        file.close()
        mixer.init()
        mixer.music.load("notification.mp3")
        mixer.music.play()
        notification.notify(
            title="My Tasks::-",
            message=content,
            timeout=20
        )




if __name__ == "__main__":
    
    with open("password.txt", "r") as pw_file:
        saved_password = pw_file.read().strip()  # Read and remove any extra whitespace or newline


    for i in range(1):
        a = input("Enter password: ")

    if a == saved_password:
        wishme() 
       
       
    else:  
        speak("Sahi Password Daal. Goodbye.")
        exit()
   
  
    
    while True:
        query = takeCommand()
        if query is None:  # Handle case where no command was recognized
            continue

        if 'wikipedia' in query.lower():
            query = query.replace("wikipedia", "")
            search_wikipedia(query)

        elif "news" in query:
            latestnews(query)

        elif "Whatsapp" in query:
            sendmessage()
        
        elif "task" in query.lower():
            SecduleMyDay(query)


        elif 'exit' in query:
            speak("Goodbye!")
            break

       
