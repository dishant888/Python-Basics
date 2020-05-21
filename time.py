from time import *
import datetime

# print('Time in format of tics: ',time())
# print('Time in format of Local: ',localtime())
# print('Time in format of Date time: ',asctime())

# 9 - 5
# 3 liters
# 500ml

lts = 3000
drink = 500
starting = int(input('Starting time: '))
ending = int(input('Ending time: ')) + 12
totalTime = ending - starting
totalInterval = int(lts/drink)
timeInterval = totalTime/totalInterval
print(timeInterval)