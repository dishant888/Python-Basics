# Print only numeric values from list

collection = ['hello',12,'BCA',12.34,1,3,'Python']

for i in collection:
    if isinstance(i,float) or isinstance(i,int):
        print(i)