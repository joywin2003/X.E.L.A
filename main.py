import speech_recognition as sr
import os

def say(text):
    os.system("say " + text)

if __name__ == '__main__':
    say("Hey Mansur Bhai, how are you doing with your girlfriend?")
