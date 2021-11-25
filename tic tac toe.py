# TIC TAC TOE GAME

print('\n\t\t\t\t\t\t\t\t\tTIC TAC TOE GAME !!!!!!!')


def draw_board(b):
    print('\n')
    print('\t\t'+b[0]+'\t\t|\t\t'+b[1]+'\t\t'+'|\t\t'+b[2])
    print('\t------------|---------------|--------------')
    print('\t\t'+b[3]+'\t\t|\t\t'+b[4]+'\t\t'+'|\t\t'+b[5])
    print('\t------------|---------------|--------------')
    print('\t\t'+b[6]+'\t\t|\t\t'+b[7]+'\t\t'+'|\t\t' + b[8])
    print('\n\n')


board = [' ']*9
draw_board(board)

name_1 = input('Player-1, Enter your name:')
name_2 = input('Player-2,Enter your name:')
symbol_1 = input(f'{name_1},enter your symbol choice(X/0):')
if symbol_1 == 'X':
    symbol_2 = '0'
    print(f'{name_2},your symbol is: 0\n')
else:
    symbol_2 = 'X'
    print(f'{name_2},your symbol is: X\n')


def check_1(input_1):
    if board[input_1] == ' ':
        board[input_1] = symbol_1
    else:
        print('\ninvalid position!!!\n')
        take_input_1()


def check_2(input_2):
    if board[input_2] == ' ':
        board[input_2] = symbol_2
    else:
        print('\ninvalid position!!!\n')
        take_input_2()


def take_input_1():
    in_1 = int(input(f"{name_1}, it's your turn:"))
    input_1 = in_1-1
    check_1(input_1)


def take_input_2():
    in_2 = int(input(f"{name_2}, it's your turn:"))
    input_2 = in_2-1
    check_2(input_2)


def check_win():
    if board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
        return 'X'
    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        return 'X'
    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
        return 'X'
    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
        return 'X'
    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
        return 'X'
    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
        return 'X'
    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
        return 'X'
    elif board[0] == '0' and board[4] == '0' and board[8] == 'X':
        return '0'
    elif board[2] == '0' and board[4] == '0' and board[6] == '0':
        return '0'
    elif board[0] == '0' and board[3] == '0' and board[6] == '0':
        return '0'
    elif board[1] == '0' and board[4] == '0' and board[7] == '0':
        return '0'
    elif board[2] == '0' and board[5] == '0' and board[8] == '0':
        return '0'
    elif board[0] == '0' and board[1] == '0' and board[2] == '0':
        return '0'
    elif board[3] == '0' and board[4] == '0' and board[5] == '0':
        return '0'
    elif board[6] == '0' and board[7] == '0' and board[8] == '0':
        return '0'
    else:
        return 'd'


a = 0
while a < 4:
    take_input_1()
    draw_board(board)
    win = check_win()
    if win == symbol_1:
        print('\n\tCONGRATULATIONS!!! Player-1 you win.......')
        exit()
    take_input_2()
    draw_board(board)
    win = check_win()
    if win == symbol_2:
        print('\n\tCONGRATULATIONS!!! Player-2 you win.......')
        exit()
    a += 1

    if win == 'd':
        print('\n\t MATCH DRAW.....')
