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