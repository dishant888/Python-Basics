# Exception Handling

# 1) Compile time error (eg syntax)
# 2) Logical error
# 3) Run time error (eg 1/0)

# a,b = int(input('Enter 1st no: ')), int(input('Enter 2nd no: '))
# try:
#     print(a/b)
# except Exception as e:
#     print('Error: ',e)

#------------------------------------------------------------------------

# try:
#     char = int(input('Enter character: '))
# except Exception as e:
#     print(e)

#------------------------------------------------------------------------

# a,b = int(input('Enter 1st no: ')), int(input('Enter 2nd no: '))
# try:
#     print(a/b)
#     x = int(input('Enter no: '))
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as v:
#     print(v)
# except Exception as Ex:
#     print(Ex)
# finally:
#     print('Inside Finally')

#------------------------------------------------------------------------

from time import *

# print(asctime(localtime(time())))

# print(time())
# start = time()
# print('Dishant')
# sleep(2)
# print('Sachin')
# sleep(1)
# print('Shubham')
# print(time())
# end = time()
# print('Difference: ',end-start)

import datetime
# print(datetime.datetime.now())

#------------------------------------------------------------------------

#Diff in time

# if datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day,8) > datetime.datetime.now() >  datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day,16):
#     print('Between 8 and 4')
# else:
#     print('After 4')
#     print(datetime.datetime.now())

#------------------------------------------------------------------------

from calendar import *

# Print calender particular Month of year
# cal = month(2020,5)
# print(cal)

# Print whole year calender
prcal(2020)

#------------------------------------------------------------------------