import os
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from openai import OpenAI

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a smart AI assistant. Reply briefly."},
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content

def processCommand(cmd):
    if "open google" in cmd.lower():
        webbrowser.open("https://google.com")
    else:
        reply = aiProcess(cmd)
        speak(reply)

if __name__ == "__main__":
    speak("Assistant started")
