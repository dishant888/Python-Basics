# Convert number to words (0-999999999)

ones = {
    0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight',9:'Nine'
}

tens = {
    10:'Ten', 11:'Eleven', 12:'twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen',
    17:'Seventeen', 18:'Eighteen', 19:'Nineteen'
}

preDefined = {
    2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
    6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
}

combined = {}
combined.update(ones)
combined.update(tens)

ending = {
    7:'crore', 5:'lakh', 3:'thousand', 2:'hundread', 0:''
}

def inWords(number):
    result = ''
    if number == 0:
        result = 'Zero'
    else:
        power = 7
        while number > 0:
            div = 10 ** power
            digits = number // div

            if digits in combined.keys():
                if digits != 0:
                    result += combined[digits] + " " + ending[power] + " "
            else:
                firstDigit = preDefined[digits // 10]
                secondDigit = ones[digits % 10]
                result += firstDigit + " " + secondDigit +" "+ ending[power]+" "

            if power == 3:
                power -= 1
            else:
                power -= 2

            number %= div
    return result

if __name__ == '__main__':

    print(inWords(256))
    print(inWords(100))
    print(inWords(56))
    print(inWords(40))
    print(inWords(4))
    print(inWords(12))
    print(inWords(101))
    print(inWords(111))
    print(inWords(190))
    print(inWords(99))
    print(inWords(999))
    print(inWords(0))
    print(inWords(1000))
    print(inWords(1001))
    print(inWords(1011))
    print(inWords(1030))
    print(inWords(9430))
    print(inWords(6543))
    print(inWords(10000))
    print(inWords(10999))
    print(inWords(999999999))