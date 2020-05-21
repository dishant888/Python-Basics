# File Handling

# Modes
# 'r' = read
# 'w' = write
# 'a' = append
# 'x' = create file if not exists
# 't' = text mode
# 'b' = binary
# 'r+' = read + write

#------------------------------------------------------------------------

# read:
# f = open('files/demo.txt','r')
# print(f.read()) # read whole file
# # print(f.readline()) # read line
# # print(f.readline(9)) # read n char of line

#------------------------------------------------------------------------

# write:
# f = open('files/demo1.txt','w')
# f.write('This is written with program')

#------------------------------------------------------------------------

# read:
# f = open('files/demo3.txt','r')
# content = str(f.read())
# for i in content:
#     if i > 'A' and i < 'Z':
#         print(i,end=' ')

#------------------------------------------------------------------------

# read + write:
# f = open('files/demo4.txt','r+')
# print(f.read())
# f.write('This line is written from program')
# print(f.read())
# print(f.tell()) # count char
# print(f.seek(10)) # cursor to 10th position
# print(f.readline()) # read line from 10th position

#------------------------------------------------------------------------

# ques
#1 copy content from one file to another
#2 copy content from one file to another in reverse order
#3 copy img from one to another location