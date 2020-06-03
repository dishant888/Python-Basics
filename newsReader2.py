import requests

def Speak(str):
    from win32com.client import Dispatch
    d = Dispatch("SAPI.SpVoice")
    d.Speak(str)

Speak('News for today.Lets start')

url = 'http://newsapi.org/v2/everything?q=apple&from=2020-05-31&to=2020-05-31&sortBy=popularity&apiKey=5088b37404fa417bb5631543b72915d5'

res = requests.get(url).json()
articles = res['articles']
print(articles)

for article in articles:
    print(article['title'])
    Speak(article['title'])
    Speak('Moving to  the next news')