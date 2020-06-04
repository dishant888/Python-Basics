
moves = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

def Board():
    print(f'\t\t\t {moves[0]} | {moves[1]} | {moves[2]} ')
    print('\t\t\t-----------')
    print(f'\t\t\t {moves[3]} | {moves[4]} | {moves[5]} ')
    print('\t\t\t-----------')
    print(f'\t\t\t {moves[6]} | {moves[7]} | {moves[8]} ')

Board()

winPattern = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def checkWin(turn):
    for i in winPattern:
        if moves[i[0]] == turn and moves[i[1]] == turn and moves[i[2]] == turn:
            return True

turn = 'X'
i = 0
while i < 9:
    move = int(input(f"{turn}'s Turn: "))
    if moves[move] == ' ':
        moves[move] = turn
        i += 1
        if checkWin(turn):
            str = ' ' + turn + ' wins '
            print(str.center(33, '#'),'\n')
            Board()
            print('\n', str.center(33, '#'))
            break
        else:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            Board()
    else:
        print('This place is occupied by',moves[move])
else:
    print(' Tie '.center(33,'#'),'\n')
    Board()
    print('\n',' Tie '.center(33,'#'))