# Gusess the no in given chances

n = int(input('Enter number: '))
chances = int(input('Enter number of guesses: '))

while(chances > 0):
    guess = int(input('Enter your guess: '))
    if guess > n:
        print('Number is smaller than ',guess)
    elif guess < n:
        print('Number is greater than ', guess)
    else:
        print('You Won')
        break
    chances -= 1
    print('Chances left: ',chances)
else:
    print('You lost')