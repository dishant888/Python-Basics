'''
is also used as pre format text
'''

# str = '''
#         this is is
#         dummy text
#     '''
# print(str)

#------------------------------------------------------------------------

# list is collection of elements (dissimilar)

# Index: (1) 0 to n-1
#        (2) -1 to -n
# slicing
# dynamic memory allocation (declaring size not required)
# Multi list can be designed (list within list)
#list is mutable(updatable) and string is unmutable

#------------------------------------------------------------------------

# list = [1,2,3,4,5,6,7]
# list[1] = 100
# print(list)

#------------------------------------------------------------------------

# list2 = [101,'Dishant','BCA','90%','RAJASTHAN']
# a = 10
# print(type(list2),type(a))
# print(list2[1])
# print(list2[0:2])  #0 is included 2 is excluded
# print(list2[::-1])  #reverse

# print(list+list2) #concanate

#------------------------------------------------------------------------

#List within list
# list2 = ['first','second','third']
# list1 = [1,2,3,['one','two','Three'],list2]
# for item in list1:
#     print(item)

#------------------------------------------------------------------------

# a = [10,20,30,40,50,60,70,80]

#working with index

# for i in range(0,8):
#     print(a[i])
#
# print('\n')
#
# for i in range(0,8,2):
#     print(a[i])
#
# print('\n')
#
# for i in range(5): #0 to <5
#     print(a[i],end=",") #separated by (,)
# print('\b')

# for i in range(len(a)):
#     print(a[i])

# for i in range(len(a)-1,-1,-1): #reverse
#     print(a[i])


#working with element

# for item in a:
#     print(item)
#     #print(item+item)
#     # print(item)

#------------------------------------------------------------------------

# print(int.__add__(3,4))

#------------------------------------------------------------------------

#Insert

# a = []
# n = int(input('Enter no of elements: '))
#
# for i in range(n):
#     data = int(input('Enter element: '))
#     a.append(data)

# print(a)

#------------------------------------------------------------------------

#Search

# item = int(input('Enter data to search: '))

# if(item in a):
#     print(item,' Found at ',a.index(item))
# else:
#     print('Not Found')

#or (freq of item)

# if(a.count(item)):
#     print(item,' Found ',a.count(item),' times')
# else:
#     print('Not Found')

#------------------------------------------------------------------------

# a = [1,2,3,4,5]
# b = [6,7,8,9,0]
# a.extend(b) #append items of b in a
# print(a)
# a.clear() #clear all items
# print(a)
# a.insert(1,200) #add new(200) item at index(1)
# print(a)
# a.remove(5) #value to remove
# print(a)
# a.pop(3) #remove element at index(3)
# print(a)
# del a[2:5] #dlete from index(2) to index(5)
# print(a)

# c = [43,23,56,3,7,12,62,25]
# print(min(c)) #print minimum
# print(max(c)) #print max
# print(sum(c)) #sum
# c.sort() #ascending sort
# print(c)

#------------------------------------------------------------------------

#Insert new element

# a = []
# size = int(input('Enter size: '))
#
# for i in range(size):
#     data = (input('Enter data: '))
#     a.append(data)
#
# print(a)
#
# newVal = int(input('Enter new value to insert: '))
# pos = int(input('Enter position to insert: '))
#
# a.insert(pos-1,newVal)
#
# print(a)

#------------------------------------------------------------------------

