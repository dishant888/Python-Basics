# Greet

import pyttsx3
# import pywin32
import pythoncom
import datetime

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice',voice[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    h = datetime.datetime.now().hour
    speak('Hi Dishant!')
    if h > 0 and h < 12:
        speak('Good moring')
    elif h > 12 and h < 18:
        speak('Good noon')
    elif h > 18 and h < 20 :
        speak('Good evening')
    else:
        speak('Good night')

greet()

import speech_recognition as sr

def takeCmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1 # Speaking speed
        audio = r.listen(source)
        print(audio)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-IN')
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)
        print('Speak Again')
        return 'None'
    return query

var = takeCmd().lower()
speak(var)

import wikipedia
import webbrowser
import os

if 'wikipedia' in var:
    print('Im searching in wikipedia.....')
    speak('Im searching in wikipedia')
    var = var.replace('wikipedia','')
    result = wikipedia.summary(var,sentences=2)
    print(f'According to wikipedia {result}')
    speak(f'According to wikipedia {result}')
elif 'open youtube' in var:
    print('Opening Youtube...')
    speak('Opening Youtube...')
    webbrowser.open('youtube.com')
elif 'open google' in var:
    print('Opening Google...')
    speak('Opening Google...')
    webbrowser.open('google.com')
elif 'time' in var:
    print(f'Time is: {datetime.datetime.now().strftime("%H:%M:%S")}')
    speak(f'Time is: {datetime.datetime.now().strftime("%H:%M:%S")}')
elif 'song' in var:
    directory = 'E:\\songs\\'
    songs = os.listdir(directory)
    print(songs)
    os.startfile(os.path.join(directory,songs[0]))