#1

# a, b = int(input('Enter a: ')), int(input('Enter b: '))

# if a>b:
#     print(a,' is greater')
# else:
#     print(b,' is greater')

#Single if
#if a>b: print(a,' is greater')

#pass (keyword)
# if(a>b):
#     pass
# else
#     print(b,' is greater')

#NOT,AND,OR
# if not a>b:
#     print(b,' is greater')
# else:
#     print(a,' is greater')

#ternary operator
# true if condition else false
# print(a,' is greater') if a>b else print(b,' is greater')

#----------------------------------------------

#2

# ch = input('Enter Character: ')[0] #first letter(slicing)
# ch = ch.upper()
# if(ch in 'A,E,I,O,U'):
#     print('Vowel')
# else:
#     print('Not Vowel')

'''
   -6 -5 -4 -3 -2 -1
    R  A  M  E  S  H
    0  1  2  3  4  5
'''

#-----------------------------------------------

#3

# name = input('Enter name: ')
#0 1 2
# print(name[0:3])

#0 2 3 6
# print(name[0:6:2])

#-----------------------------------------------

#4

# a, b, c = int(input('Enter a: ')), int(input('Enter b: ')), int(input('Enter c: '))
#
# if a>b:
#     if a>c:
#         print(a,' is greatest')
#     else:
#         print(b,' is greatest')
# else:
#     if b>c:
#         print(b,' is greatest')
#     else:
#         print(c,' is greatest')

#-------------------------------------------------

#5

# a, b, c = int(input('Enter a: ')), int(input('Enter b: ')), int(input('Enter c: '))
#
# ans = a if a>b else b if b>c else c
#
# print(ans,' is greatest')

#--------------------------------------------------

#6

# a, b, c = eval(input('Enter three numbers separated by commas (,): '))
# if a>b and a>c:
#     print(a,' is greatest')
# elif b>a and b>c:
#     print(b,' is greatest')
# else:
#     print(c,' is greatest')

#-----------------------------------------------

#7

# name = 'rAmeShawAR'
#
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name.count('m'))
# print(name.title())
# print(name.center(22,'*'))
#
# string = 'Python is best programming language Python Python'
#
# print(string)
# print(string.replace('Python','Django'))
# print(string.replace('Python','Django',2))

#----------------------------------------------
