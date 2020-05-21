#Convert Amt to notes

amt = int(input('Enter Amount: '))
t = amt

twoThousands = amt//2000
amt = amt - twoThousands * 2000
#or
#amt = amt%2000
print('2000 \t*\t ',twoThousands,' \t=\t ',twoThousands * 2000)

fiveHundred = amt//500
amt -= fiveHundred * 500
print('500 \t*\t ',fiveHundred,' \t=\t ',fiveHundred * 500)

twoHundred = amt//200
amt -= twoHundred * 200
print('200 \t*\t ',twoHundred,' \t=\t ',twoHundred * 200)

oneHundred = amt//100
amt -= oneHundred * 100
print('100 \t*\t ',oneHundred,' \t=\t ',oneHundred * 100)

fifty = amt//50
amt -= fifty * 50
print('50 \t\t*\t ',fifty,' \t=\t ',fifty * 50)

twenty = amt//20
amt -= twenty * 20
print('20 \t\t*\t ',twenty,' \t=\t ',twenty * 20)

ten = amt//10
amt -= ten * 10
print('10 \t\t*\t ',ten,' \t=\t ',ten * 10)

five = amt//5
amt -= five * 5
print('5 \t\t*\t ',five,' \t=\t ',five * 5)

two = amt//2
amt -= two * 2
print('2 \t\t*\t ',two,' \t=\t ',two * 2)

one = amt//1
print('1  \t\t*\t ',one,' \t=\t ',one * 1)

print('______________________________')
print('\t\t\t\t\t\t',t)