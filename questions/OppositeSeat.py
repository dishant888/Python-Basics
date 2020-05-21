# Find the opposite seat form the given arrangement
#  1  2  3  4  5  6
#
# 12 11 10  9  8  7
# 13 14 15 16 17 18
#
# 24 23 22 21 20 19
#eg: input = 4 opposite seat = 9
#    input = 20 opposite seat = 17

seat = int(input('Enter seat: '))
diff = [11,9,7,5,3,1]

if seat % 12 in [1,2,3,4,5,6]:
    oppositeSeat = seat + diff[(seat%12)-1]
else:
    oppositeSeat = seat - diff[12 - (seat%12)]

print('Opposite seat: ',oppositeSeat)

#----------------------------------------------------------

# seat = int(input('Enter seat: '))
# diff = [11,9,7,5,3,1,1,3,5,7,9,11]
#
# if seat % 12 in [1,2,3,4,5,6]:
#     oppositeSeat = seat + diff[(seat%12)-1]
# else:
#     oppositeSeat = seat - diff[(seat%12)-1]
#
# print('Opposite seat: ',oppositeSeat)

#----------------------------------------------------------