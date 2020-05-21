#Convert seconds to 24hr format

sec = int(input('Enter seconds: '))

hrs = sec//(60*60)
sec -= 3600 * hrs #or sec %= 3600

min = sec//60
sec -= 60 * min #or sec %= 60

print(hrs,':',min,':',sec)