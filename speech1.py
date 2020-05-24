# Assistant

import pyttsx3 # Python Text To Speech 3
# import pywin32 # (Python Commands are in this module)
import pythoncom # (Python Commands from pywin32)


try:
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')
    # print(voice[0].id)
    engine.setProperty('voice', voice[0].id)
except Exception as e:
    print(e)
else:
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    speak('My name is Dishant')