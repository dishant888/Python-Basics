# Array
from array import * # { len() }
# or
# import array  # { array.len() }

# vals = array('i',[1,2,3,4,5])
# print(vals.buffer_info()) # base address, count of elements

# print elements:
# for i in vals:
#     print(i)
# or
# for i in range(len(vals)):
#     print(i,':',vals[i])

#------------------------------------------------------------------------

# linear search

# vals = array('i',[])
#
# n = int(input('Enter no of elemnts: '))
# for i in range(n):
#     vals.append(int(input('Enter no: ')))
#
# data = int(input('Enter data to search: '))
#
#or
# if data in vals:
#     print('found at',vals.index(data))
# else:
#     print('Not Found')

# for i in vals:
#     if i == data:
#         print(data,' found at ',vals.index(i)+1)
#         break
# else:
#     print(data,' not found')

#------------------------------------------------------------------------

# delete element from array

# vals = array('i',[])
#
# n = int(input('Enter no of elemnts: '))
# for i in range(n):
#     vals.append(int(input('Enter no: ')))
#
# delete1 = int(input('Enter element to delete: '))
#
# vals.remove(delete1)
# print(vals)

#------------------------------------------------------------------------

# remove repetetions from array

# vals = array('i',[])

# n = int(input('Enter no of elemnts: '))
# for i in range(n):
#     vals.append(int(input('Enter no: ')))
#
# for i in vals:
#     print(vals.count(i),end=",")

#------------------------------------------------------------------------

# arr1 = array('i',[1,2,3,4,5,6])
# arr2 = array('i',[])
#
# for i in arr1:
#     arr2.append(int(i)*2)
#
# print(arr2)

#or
# arr2 = list(map(lambda a:a*2,arr1))
# print(arr2)

# Sum
# from functools import reduce
#
# sum = reduce(lambda a,b:a+b,arr1)
#
# print(sum)

#filter
# arr2 = list(filter(lambda a:not a%2,arr1))
# print(arr2)
#------------------------------------------------------------------------

#Min from array

# arr1 = array('i',[35,21,5461,43,20,21,-3,-12])
#
# min = min(arr1)
#
# print(min)

#------------------------------------------------------------------------

#Sum from array

# arr1 = array('i',[35,21,5461,43,20,21,-3,-12])
#
# print(sum(arr1))

#------------------------------------------------------------------------