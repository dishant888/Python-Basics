# Functions (block of code, can be called multiple times, also known as module)
# 1 Pre defined (some functions needs header files or imports)
# 2 User defined

#-------------------------------------------------------------------------

#Add 2 nos

# def MySum(x,y):
#     return x+y
#
# a,b = int(input('Enter number: ')), int(input('Enter number: '))
# print(MySum(a,b))

#-------------------------------------------------------------------------

# Compare first and last

# string = input('Enter String: ')
# if string[0] == string[-1]:
#     print("First and last are Equal")
# else:
#     print("Not Equal")

#through function

# def first(string):
#     return string[0]
# def last(string):
#     return string[-1]
# if(first(string) == last(string)):
#     print('Equal')
# else:
#     print('Not Equal')

#-------------------------------------------------------------------------

#Swap

# a,b = int(input()), int(input())
#
# def swap():
#     global a,b
#     a,b = b,a
#     print("A:",a,"b:",b)
# swap()
# print("A:",a,"b:",b)

#-------------------------------------------------------------------------

#list is always global

# def update(list1):
#     for i in range(5):
#         list1[i] += 10
#     print(list1)
#
# list1 = [1,2,3,4,5]
# update(list1)
# print(list1)

#-------------------------------------------------------------------------

# Swapping with list

# def swap(list):
#     list[0],list[1] = list[1],list[0]
#
# list = [1,2]
# swap(list)
# print(list)

#-------------------------------------------------------------------------

#Keywords

# def show(name,age):
#     print(name,age)
#
# # name,age = input('Enter name:'), int(input('Enter age: '))
# show(age=25,name='Rahul')

#-------------------------------------------------------------------------

#Default Args

# def show(name,age=30):
#     print(name,age)
#
# show(name='Rahul')

#-------------------------------------------------------------------------

#Variable length
#ADD 1,2,3,4,5

# def add(a,*b): #a=1, b=2-5(tuple)
#     # print(a,b)
#     c = a
#     for i in b:
#         c += i
#     return c
##or
# def add(*b): #b=1-5(tuple)
#     # print(b)
#     c = 0
#     for i in b:
#         c += i
#     return c
#
# print(add(1,2,3,4,5))

#-------------------------------------------------------------------------

# def person(name,**data): # **data{Dict.}
#     print(name)
#     print(data)
#     for i,j in data.items():
#         print(i,j)
#
# person("Ram",age=28,city="UDPR",moblie='1234567890')

# age 28
# city udpr
# mob ....

#-------------------------------------------------------------------------

# Sort

# students = []
# n = int(input('Enter number of inputs: '))
# for i in range(n):
#     students.append(input('Enter name: '))
#
# def sort(students):
#     for i in range(n):
#         for j in range(i+1,n):
#             if students[i] > students[j]: #(will compare each letter) ## note: if students[i][0] > students [j][0] (will compare firts letter)
#                 students[i],students[j] = students[j],students[i]
#     return students
#
# print(sort(students))
# print(students.sort()) #pre defined

#-------------------------------------------------------------------------
#1) enter msg           'My name is dishant'
#2) word to encode      'BCA'
#                       'O '
# if greater than 26 (%26)
# print(ascii(a))

#-------------------------------------------------------------------------

#Encode and Decode

# msg = input('Enter message: ')
# encodingWord = input('Enter encoding word: ')
#
# def encode(msg,encodingWord):
#     newString = ''
#     for i in range(len(msg)):
#         letterOfMsg = msg[i]
#         letterOfEncodingWord = encodingWord[i % len(encodingWord)]
#         sum = ord(letterOfMsg) + ord(letterOfEncodingWord)
#         newString += chr(sum)
#     return newString
#
# def decode(encodedString,encodingWord):
#     newString = ''
#     for i in range(len(encodedString)):
#         letterOfMsg = encodedString[i]
#         letterOfEncodingWord = encodingWord[i % len(encodingWord)]
#         diff = ord(letterOfMsg) - ord(letterOfEncodingWord)
#         newString += chr(diff)
#     return newString
#
# encodedString = encode(msg,encodingWord)
#
# print(encodedString)
# print(decode(encodedString,encodingWord))

#-------------------------------------------------------------------------