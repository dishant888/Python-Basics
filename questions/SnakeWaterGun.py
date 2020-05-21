#Snake Water Gun Game

import random

# list1 = ['Snake','Water','Gun']
# chances = 0
# playerWins = 0
# computerWins = 0
# while(chances != 10):
#     player = random.choice(list1)
#     computer = random.choice(list1)
#     if player == computer:
#         print('Tie')
#     else:
#         chances += 1
#         if player == 'Snake' and computer == 'Water':
#             playerWins += 1
#             print('player wins')
#         elif player == 'Gun' and computer == 'Water':
#             computerWins += 1
#             print('computer wins')
#         elif player == 'Water' and computer == 'Gun':
#             playerWins += 1
#             print('player wins')
#         elif player == 'Water' and computer == 'Snake':
#             computerWins += 1
#             print('computer wins')
#         elif player == 'Snake' and computer == 'Gun':
#             computerWins += 1
#             print('computer wins')
#         elif player == 'Gun' and computer == 'Snake':
#             playerWins += 1
#             print('player wins')
# print('Player Total: ',playerWins)
# print('Computer Total: ',computerWins)

#=----------------------------------------------------------------------

moves = ['Snake','Water','Gun']
playerWinPattern = [['Snake','Water'],['Water','Gun'],['Gun','Snake']]

chances = 0
computerScore = 0
playerScore = 0

while chances != 10:
    player = random.choice(moves)
    computer = random.choice(moves)
    if player == computer:
        print('Player: ',player,' Computer: ',computer,'[Tie]','(Computer(',computerScore,'))','(Player(',playerScore,'))')
    else:
        if [player,computer] in playerWinPattern:
            playerScore += 1
            print('Player: ', player, ' Computer: ', computer, '[Player Wins]', '(Computer(', computerScore, '))', '(Player(',playerScore, '))')
        else:
            computerScore += 1
            print('Player: ', player, ' Computer: ', computer, '[Computer Wins]', '(Computer(', computerScore, '))',
                  '(Player(', playerScore, '))')
        chances += 1