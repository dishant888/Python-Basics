# Loop for, while and do-while

#Prime
# n = int(input('Enter Number: '))
# s = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         s += 1
#
# if s==2:
#     print('Prime')
# else:
#     print('Not Prime')

##or

# n = int(input('Enter Number: '))
# s = 0
# for i in range(2,(n//2)+1):
#     if n%i == 0:
#         print('Not Prime')
#         break
# else:
#     print('Prime')

#-----------------------------------------------------------------------

#Factorial

# n = int(input('Enter number: '))
# fact = 1
# for i in range (1,n+1):
#     fact *= i
#
# print('Factorial: ',fact)

#-----------------------------------------------------------------------

#Perfect

# n = int(input('Enter number: '))
# sum = 0
#
# for i in range(1,n):
#     if(n%i==0):
#         sum += i  # sum = sum + i
#
# if(sum == n):
#     print('Perfect')
# else:
#     print('Not Perfect')

#-----------------------------------------------------------------------

#Addition of n nos

# sum = 0
# for i in range (10):
#     n = int(input('Enter number: '))
#     sum += n
#
# print('Sum: ',sum)

#-----------------------------------------------------------------------

#Febonacci
# n=5, 0,1,1,2,3,5

# a = 0
# b = 1
#
# n = int(input('Enter range: '))
# print('0,1',end=',')
# for i in range(n-2):
#     c = a+b
#     print(c,end=",")
#     a = b
#     b = c
#     ##or
#     # print(a + b, end=",")
#     # a, b = b, a + b

#-----------------------------------------------------------------------

#Table

# n = int(input('Enter number: '))
#
# for i in range(1,11):
#     print(i,'x',n,'=',n*i)

#-----------------------------------------------------------------------

# sum = 0
# list = []
# for i in range(1,11):
#     n = int(input('Enter no: '))
#     sum = n-1 + n + n+1
#     list.append(sum)
#
# print(list)

#-----------------------------------------------------------------------

# str1 = "My name is dishant dishant is doing BCA dishant is playing nationls"
# # print(str.count('dishant'))
# # print(str1.replace('dishant','ram'))
#
# str2 = input('Enter name to search: ')
# count = 0
# for i in range(0,len(str1)):
#     # count += str1[i:i + len(str2)] == str2
#     #or
#     if(str1[i:i+len(str2)]==str2):
#         count += 1
#
# print(count)

#-----------------------------------------------------------------------
# str1 = "My name is dishant dishant is doing BCA dishant is playing nationals"
#
# str2 = input('Enter string to replace: ')
#
# new = input('Enter string to replace with: ')

# split string into list [ list = str1.split() ]:-
# word = ''
# list = []
# for i in str1:
#     if i != ' ':
#         word += i
#     else:
#         list.append(word)
#         word = ''
# list.append(word)
# # print(list)
# # split end ------
#
#
# # Update with new string:
# str1 = ''
# for i in range(len(list)):
#     if list[i] == str2:
#         list[i] = new
#     str1 += list[i] + ' '
#
# print(str1)
#Update end

#or

# "My name is dishant dishant is doing BCA dishant is playing nationals"

# word = ''
# newStr = ''
# for i in str1:
#     if i != ' ':
#         word += i
#     else:
#         if word == str2:
#             word = new
#
#         newStr += word + ' '
#         word = ''
#
# if word == str2:
#     newStr += new
# else:
#     newStr += word
#
# str1 = newStr
#
# print(str1)

#-----------------------------------------------------------------------

#While

# i = 10
# while (i>=1):
#     print(i)
#     i-=1

#-----------------------------------------------------------------------

#sum of every digit

# 2134 = 10
#153 = 1 + 125 + 27 = 153
# sum = 0
# n = int(input('Enter no: '))
# a = n
# while(n!=0):
#     digit = n%10
#     sum = sum + digit**3
#     n = n//10
# if a == sum:
#     print('Armstrong')
# else:
#     print('Not Armstrong')
# print(sum)
##or
# n = input('Enter no: ')
# sum = 0
# for i in n:
#     sum = sum + int(i)
#
# print(sum)

#-----------------------------------------------------------------------

#Magic no
#81 8+1 = 9 = 9*9, 1729 = 19 * 91

#1: Enter no
#2: Sum of digits
#3: reverse
#4: sum of digit * reverse == real no

# n = input('Enter no: ')
#
# sum = 0
# for i in n:
#     sum = sum + int(i)
#
# n1 = sum
# n2 = sum
# sum = 0
# while(n1!=0):
#     digit = n1%10
#     sum = sum * 10 + digit
#     n1 = n1//10
#
# if sum*n2 == int(n):
#     print('Magic no')
# else:
#     print('Not Magic no')

#-----------------------------------------------------------------------

#Strong no

#145 = 1!(1) + 4!(24) + 5!(120) = 145

# n = int(input('Enter no: '))
# a = n
# fact = 1
# sum = 0
# while(n!=0):
#     digit = n%10
#     fact = 1
#     for i in range(1,digit+1):
#         fact *= i
#     sum += fact
#     n = n//10
# if sum == a:
#     print('Strong no')
# else:
#     print('Not Strong no')

#-----------------------------------------------------------------------

#1 to 100 prime no

# for j in range(1,101):
#     n = j
#     sum = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             sum = sum +1
#     if sum == 2:
#         print(n,end=',')

#-----------------------------------------------------------------------

#Nested Loop (loop within loop)

#Star Printing

"""
*****
*****
*****
*****
*****
"""
# for i in range(5):
#     for j in range(5):
#         print('*',end=" ")
#     print('\n')

#-----------------------------------------------------------------------

# for i in range(1,6):
#     print('*'*i)

#-----------------------------------------------------------------------

      #   * *   * *
      # *     *     *
      #   *       *
      #     *    *
      #        *

# for i in range(5):
#     for j in range(7):
#         if ((i == 0 and j%3 != 0) or (i == 1 and j%3 == 0) or (i - j == 1) or (i+j==7)):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#-----------------------------------------------------------------------

        #     1
        #    121
        #   12321
        #  1234321
        # 123454321

# for i in range(1,6):
#     print(' '*(5-i),end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     for k in range(i-1,0,-1):
#         print(k,end='')
#     print()

#-----------------------------------------------------------------------