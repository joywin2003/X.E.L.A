import speech_recognition as sr
import os

def say(text):
    os.system("say " + text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query


if __name__ == '__main__':
    say("Hello, my name is Jarvis. What can I do for you?")
    print("Listening...")
    text = takeCommand()
    say(text)
