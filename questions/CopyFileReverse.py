# Copy one file (files/CopyFromRev) to another file (files/CopyToRev) in reverse order

CopyFrom = open('files/CopyFromRev','r')
content = str(CopyFrom.read())
reverse = ''
for i in range(len(content)-1,-1,-1):
    reverse += content[i]

CopyTo = open('files/CopyToRev','w')
CopyTo.write(reverse)
CopyTo = open('files/CopyToRev','r')
print(CopyTo.read())