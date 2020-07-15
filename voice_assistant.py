# -*- coding: utf-8 -*-
"""Voice Assistant.ipynb

import pyttsx3
import datetime
import selenium
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sanyam")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sanyam")
    else:
        speak("Good evening Sanyam")
    speak("Hello I am your personal assistant. Please tell me how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recogonizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    except Exception:
        print("Please say again")
        return ("None")
    return query
if __name__=="__main__":
    speak("Hello Sir. I am Friday and today is a very nice weather")
wishme()
query=takeCommand()
query=query.lower()
if 'wikipedia' in query:
        speak("Searching Wikipedia.....")
        query= query.replace("Wikipedia",'')
        results = wikipedia.summary(query,sentences=10)
        speak("According to Wikipedia ")
        print(results)
        speak(results)
elif "open youtube" in quer6thy:
        webbrowser.open("youtube.com")
elif "open google"  in query:
        webbrowser.open("google.com")    
elif "openstack"  in query:
        webbrowser.open("stackoverflow.com")
elif "play music" in query:
        music_dir='F:\\Music_1\\Atif Aslam'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:M:%S")
        speak(f"Hyy Sanyam The time is {strTime}")





