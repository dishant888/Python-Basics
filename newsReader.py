from requests import get
import pyttsx3
import datetime

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
i = 0
choice = 1
while choice == 1:

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
    speak(description)
    speak('Press 1 for next news and 0 to exit ....')
    choice = int(input())
    if choice == 1:
        i += 1
else:
    speak('Thank you! have a good day')