#Add first and last digit of 4 digit no

#First and Last Digit
n = int(input('Enter 4 digit number: '))
last = n%10
first = n//1000

print('Sum of first and last digits: ',first+last)

#All digits

d1 = n//1000
n %= 1000

d2 = n//100
n %= 100

d3 = n//10
n %= 10

print('Sum of all digits: ',d1+d2+d3+n)