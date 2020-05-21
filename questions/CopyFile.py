# Copy one File (files/CopyFrom) to another File (files/CopyTo)

CopyFrom = open('files/CopyFrom','r')
content = str(CopyFrom.read())
CopyTo = open('files/CopyTo','r+')
CopyTo.write(content)
CopyTo = open('files/CopyTo','r')
print(CopyTo.read())