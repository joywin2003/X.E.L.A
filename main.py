import speech_recognition as sr
import os
import subprocess

def say(text):
    # Escape the text properly and use subprocess to execute the say command
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
    say("Hello, my name is J.A.R.V.I.S. What can I do for you?")
    while True:
        print("Listening...")
        text = takeCommand()
        say(text)
