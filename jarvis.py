import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It takes Microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as  e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for excepting tasks based on query
        if 'wikipedia' in query:
            speak("Searching WikiPedia...")
            query = query.replace("wikipedia", "")
            resutls = wikipedia.summary(query, sentences=2)
            speak("Acoording to WikiPedia")
            print(resutls)
            speak(resutls)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com.com")

        elif 'open leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open roblox' in query:
            webbrowser.open("roblox.com")

        elif 'play music' in query:
            webbrowser.open("open.spotify.com/playlist/38mWQAGEylOPPcWfDpB6FO")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ISU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open my website data' in query:
            webbrowser.open("docs.google.com/spreadsheets/d/1GItiqUmO9O-4FJ4h-OxHUQ_o23mUs0KFvksR5KqQC7w/edit?gid=0#gid=0")

        elif 'open heer website data' in query:
            webbrowser.open("docs.google.com/spreadsheets/d/1mBWhzIHa9w31jml3b2a9clH3HxafSr3SK-bnWZalCEU/edit?gid=0#gid=0")
