# Convert number to words

ones = {
    0:'', 1:'One ', 2:'Two ', 3:'Three ', 4:'Four ', 5:'Five ', 6:'Six ', 7:'Seven ', 8:'Eight ',9:'Nine '
}

tens = {
    10:'Ten ', 11:'Eleven ', 12:'twelve ', 13:'Thirteen ', 14:'Fourteen ', 15:'Fifteen ', 16:'Sixteen ',
    17:'Seventeen ', 18:'Eighteen ', 19:'Nineteen '
}

preDefined = {
    2: 'Twenty ', 3: 'Thirty ', 4: 'Forty ', 5: 'Fifty ',
    6: 'Sixty ', 7: 'Seventy ', 8: 'Eighty ', 9: 'Ninety '
}

combined = {}
combined.update(ones)
combined.update(tens)

endingInd = {
    9:'arab ', 7:'crore ', 5:'lakh ', 3:'thousand ', 2:'hundred ', 0:''
}

endingInt = {
    9:'billion ', 6:'million ', 3:'thousand ', 2:'hundred ', 0:''
}

def inWords(number,numSys = 'INT'):
    result = ''
    if number == 0:
        result = 'Zero'
    else:
        power = 9
        while number > 0:
            div = 10 ** power
            digits = number // div

            if numSys.upper() in 'INDIAN,IND':
                if digits in combined.keys():
                    if digits != 0:
                        result += combined[digits] + endingInd[power]
                else:
                    firstDigit = preDefined[digits // 10]
                    secondDigit = ones[digits % 10]
                    result += firstDigit + secondDigit + endingInd[power]

                if power == 3:
                    power -= 1
                else:
                    power -= 2

            if numSys.upper() in 'INTERNATIONAL,INT':
                if digits in combined.keys():
                    if digits != 0:
                        result += combined[digits] + endingInt[power]
                else:
                    hundredsDigit = ones[digits // 100]
                    if hundredsDigit != '':
                        result += hundredsDigit + 'hundred '

                    lastTwoDigits = digits % 100
                    if lastTwoDigits in combined.keys():
                        result += combined[lastTwoDigits] + endingInt[power]
                    else:
                        tensDigit = lastTwoDigits % 100 // 10
                        onesDigit = lastTwoDigits % 10
                        result += preDefined[tensDigit] + ones[onesDigit] + endingInt[power]

                if power == 3:
                    power -= 1
                elif power == 2:
                    power -= 2
                else:
                    power -= 3

            number %= div
    return result

#-------------------------------------------------------------------------

if __name__ == '__main__':

    print(inWords(53345345))
    print(inWords(53345345,'IND'))
    print(inWords(1581928300))
    print(inWords(1581928300,'IND'))
    print(inWords(256))
    print(inWords(256,"IND"))
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
    print(inWords(124001))
    print(inWords(104001,'INT'))
    print(inWords(104001,'IND'))
    print(inWords(7699630))
    print(inWords(7699630,'IND'))
    print(inWords(654993))
    print(inWords(654993,'IND'))
    print(inWords(999999999))
    print(inWords(999999999,'IND'))
    print(inWords(59675478365))
    print(inWords(59675478365,'INDIAN'))
    print(inWords(9010000,'int'))
    print(inWords(9010000,'ind'))