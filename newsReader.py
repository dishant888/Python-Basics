from requests import get
import pyttsx3
import datetime
import speech_recognition as SR

eng = pyttsx3.init()
eng.setProperty('voice',eng.getProperty('voices')[0].id)

def speak(text):
    print(text)
    eng.say(text)
    eng.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour > 0 and hour < 12:
        speak('Good Morning!')
    elif hour == 12:
        speak('Good Noon!')
    elif hour > 12 and hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

greet()

url = 'http://newsapi.org/v2/everything?q=apple&from=2020-05-31&to=2020-05-31&sortBy=popularity&apiKey=5088b37404fa417bb5631543b72915d5'
speak('Please wait while we fetch news for you.......')
# print(get(url).text)

def voiceCommand():
    r = SR.Recognizer()
    with SR.Microphone() as source:
        speak('Say next news or exit...')
        print('Listening...')
        r.adjust_for_ambient_noise(source,1)
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-IN')
            print(f'User said: {query}\n')
        except Exception as e:
            print(e)
            print('Speak Again')
            return 'None'
        return query


i = 0
choice = 'next news'
while choice != 'exit':

    if choice == 'next news':
        response = get(url).json()['articles'][i] # get the first news and convert to json
        author = response['author']
        title = response['title']
        description = response['description']
        if i == 0:
            speak("Today's news are as follows: ")
        else:
            speak('Next news is: ')

        speak(title)
        speak(f'By {author}')
        speak(description[:10])
        choice = voiceCommand().lower()
        i += 1
    else:
        print('Please speak again.....')
        choice = voiceCommand().lower()
else:
    speak('Thank you! have a good day')