import speech_recognition as sr

def Recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source, duration = 1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language = 'en-IN')
        print(f'User said: {query}\n')
    except Exception as e:
        print(e)
        print('Speak Again')
        return 'None'
    return query

import pyttsx3
eng = pyttsx3.init()
eng.setProperty('voice',eng.getProperty('voices')[0].id)

def Speak(text):
    print(text)
    eng.say(text)
    eng.runAndWait()

import datetime

def Greet():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        Speak('Good Morning!')
    elif hour == 12:
        Speak('Good Noon!')
    elif hour > 12 and hour < 18:
        Speak('Good Afternoon!')
    else:
        Speak('Good Evening!')