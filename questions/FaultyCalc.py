# Faulty Calculator
# 45*3 = 555, 56+9 = 77, 56/6 = 2

exp = input('Enter expression: ')
if("45*3" in exp):
    print(555)
elif("56+9" in exp):
    print(77)
elif("56/6" in exp):
    print(2)
else:
    print(eval(exp))