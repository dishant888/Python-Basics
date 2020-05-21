#input name m1,m2,m2 calculate total & percentage

name = input('Enter Name: ')
m1 = int(input('Enter Marks 1: '))
m2 = int(input('Enter Marks 2: '))
m3 = int(input('Enter Marks 3: '))
print('\n')
print('Name: \t',name)
print('Total: \t',m1+m2+m3)
print('Per: \t',(m1+m2+m3)/3,'%')
