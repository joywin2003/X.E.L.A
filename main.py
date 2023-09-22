import speech_recognition as sr
import os
import subprocess
import webbrowser
from datetime import datetime
import openai

def say(text):
    subprocess.run(["say", text])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error has occurred, Sorry Joywin"


if __name__ == '__main__':
    say("Hey Joywin, what can I do for you today?")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = {
            "Google": "https://www.google.com",
            "Facebook": "https://www.facebook.com",
            "YouTube": "https://www.youtube.com",
            "Twitter": "https://www.twitter.com",
            "Instagram": "https://www.instagram.com",
            "LinkedIn": "https://www.linkedin.com",
            "Amazon": "https://www.amazon.com",
            "Netflix": "https://www.netflix.com",
            "GitHub": "https://www.github.com",
            "Reddit": "https://www.reddit.com",
            "Wikipedia": "https://www.wikipedia.org",
            "Stack Overflow": "https://stackoverflow.com",
            "Yahoo": "https://www.yahoo.com",
            "Apple": "https://www.apple.com",
            "Spotify": "https://www.spotify.com",
            "WhatsApp": "https://www.whatsapp.com",
        }
        for site, url in sites.items():
            if f"Open {site}".lower() in query.lower():
                say(f"Opening {site}...")
                webbrowser.open(url)
        if "good night jarvis".lower() in query.lower():
            say(f"Bye Joywin")
            exit()
        elif "the time" in query.lower():
            strftime = datetime.now().strftime("%H:%M:%S")
            say(f"sir it's {strftime}")