import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    os.system('cls')
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am kimi. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching on wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            musicpath = "C:\\Users\\jaismeebaghel\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(musicpath)
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\jaismeebaghel\\Downloads"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'date' in query:
            speak("Sorry i am not interested")
            
        elif 'time' in query:
            # Get the current time
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"madam the time is {current_time}")

        elif 'can you sing' in query:
            speak("You would not like it")

        elif 'i love you' in query:
            speak("So what? everyone loves me")
