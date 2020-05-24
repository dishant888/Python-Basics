import pyttsx3
import pythoncom

students = ['Dishant','Ram','Rohan','Aakash','Piyush']

engine = pyttsx3.init("sapi5")
voice  = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

roll = int(input('Enter roll no: '))
try:
    speak(f"Answered by {students[roll-1]}")
except Exception as e:
    speak(e)