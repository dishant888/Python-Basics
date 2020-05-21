# Fee List
list1 = [["Harry",3500],["Marry",3000],["Ram",2200],["Rohit",4500],["Jarry",1500]]
s = 0
for name,fee in list1:
    if  name[-4:] == 'arry':
        s += fee
        print(name,fee)
print('Total: ',s)