import speech_recognition as sr
import os
import subprocess
import webbrowser
from datetime import datetime
import openai
from config import API_KEY
import random


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
    "WhatsApp": "https://www.whatsapp.com",
}
applications = {
    "Terminal": "/Applications/Utilities/Terminal.app",
    "Brave": "/Applications/Brave Browser.app",
    "Google Chrome": "/Applications/Google Chrome.app",
    "Visual Studio Code": "/Applications/Visual Studio Code.app",
    "Safari": "/Applications/Safari.app",
    "Spotify": "/Applications/Spotify.app",
    "VLC Media Player": "/Applications/VLC.app",
    "QuickTime Player": "/Applications/QuickTime Player.app",
}

chatStr = ""
def chat(query):
    global chatStr
    chatStr += f"Joywin: {query}\nJarvis:"
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content":f"You are Jarvis, my personal A I assistant.{query}"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response.choices[0].message['content'])
    chatStr += response.choices[0].message['content']
    print(chatStr)
    return response.choices[0].message['content']

def ai(prompt):
    openai.api_key = API_KEY
    text = f"OpenAI response for Prompt:{prompt}\n*******************\n\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response.choices[0].message['content']
    if not os.path.exists('OpenAI'):
        os.mkdir('OpenAI')
    with open(f"OpenAI/prompt-{random.randint(0,1000)}", "w") as f:
        f.write(text)


def say(text, speed=180):
    subprocess.run(["say", f"-r {speed}", text])


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            return query
        except Exception as e:
            return "Some error has occurred, Sorry Joywin"


if __name__ == '__main__':
    say("Hello Joywin, How can I help you?")
    while True:
        query = takeCommand()
        print("Listening...")
        if "open" in query.lower():
            for site, url in sites.items():
                if f"Open {site}".lower() in query.lower():
                    say(f"Opening {site}...")
                    webbrowser.open(url)
                    
            for app, path in applications.items():
                if f"Open {app}".lower() in query.lower():
                    say(f"Opening {app}...")
                    subprocess.run(["open", path])
        elif "search" in query:
                search_query = query.replace("search", "").strip()
                search_url = f"https://www.google.com/search?q={search_query}"
                say(f"Searching for {search_query}...")
                webbrowser.open(search_url)
                            
        elif "using AI".lower() in query.lower():
            ai(query)
        elif "good night jarvis".lower() in query.lower() or "bye jarvis".lower() in query.lower():
            say(f"Good Night Joywin")
            exit()
        elif "the time" in query.lower():
            strftime = datetime.now().strftime("%H:%M:%S")
            say(f"sir it's {strftime}")
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("chatting...")
            chat(query)
    
        
