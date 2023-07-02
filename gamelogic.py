def display_board(board):
    for row in board:
        print(row)

def player_move(board):
    while True:
        row = input('Enter a row (0-2, from top to bottom)')
        col = input('Enter a column (0-2, from left to right)')
        if valid_move(board, row, col):
            board[int(row)][int(col)] = 'X'
            break
def valid_move(board, row, col):
    if not (row.isnumeric() and col.isnumeric()):
        return False
    row = int(row)
    col = int(col)
    valid_nums = [0, 1, 2]
    if row in valid_nums and col in valid_nums:
        if board[int(row)][int(col)] != '':
            return False
        else:
            return True
def check_win(board, symb):
    #Check Rows
    if board[0][0] == symb and board[0][1] == symb and board[0][2] == symb:
        return True
    if board[1][0] == symb and board[1][1] == symb and board[1][2] == symb:
        return True
    if board[2][0] == symb and board[2][1] == symb and board[2][2] == symb:
        return True
    #Check Cols
    if board[0][0] == symb and board[1][0] == symb and board[2][0] == symb:
        return True
    if board[0][1] == symb and board[1][1] == symb and board[2][1] == symb:
        return True
    if board[0][2] == symb and board[1][2] == symb and board[2][2] == symb:
        return True
    #Check Diagonals
    if board[0][0] == symb and board[1][1] == symb and board[2][2] == symb:
        return True
    if board[2][0] == symb and board[1][1] == symb and board[0][2] == symb:
        return True
    return False

def num_two_in_row(board, symb):
    num_two = 0
    #Row One
    if (board[0][0] == symb and board[0][1] == symb):
        num_two += 1
    if (board[0][0] == symb and board[0][2] == symb):
        num_two += 1
    if (board[0][1] == symb and board[0][2] == symb):
        num_two += 1
    #Row Two
    if (board[1][0] == symb and board[1][1] == symb):
        num_two += 1
    if (board[1][0] == symb and board[1][2] == symb):
        num_two += 1
    if (board[1][1] == symb and board[1][2] == symb):
        num_two += 1
    #Row Three
    if (board[2][0] == symb and board[2][1] == symb):
        num_two += 1
    if (board[2][0] == symb and board[2][2] == symb):
        num_two += 1
    if (board[2][1] == symb and board[2][2] == symb):
        num_two += 1
    #Col One
    if (board[0][0] == symb and board[1][0] == symb):
        num_two += 1
    if (board[0][0] == symb and board[2][0] == symb):
        num_two += 1
    if (board[1][0] == symb and board[2][0] == symb):
        num_two += 1
    #Col Two
    if (board[0][1] == symb and board[1][1] == symb):
        num_two += 1
    if (board[0][1] == symb and board[2][1] == symb):
        num_two += 1
    if (board[1][1] == symb and board[2][1] == symb):
        num_two += 1
    #Col Three
    if (board[0][2] == symb and board[1][2] == symb):
        num_two += 1
    if (board[0][2] == symb and board[2][2] == symb):
        num_two += 1
    if (board[1][2] == symb and board[2][2] == symb):
        num_two += 1
    #Diagonal One
    if (board[0][0] == symb and board[1][1] == symb):
        num_two += 1
    if (board[0][0] == symb and board[2][2] == symb):
        num_two += 1
    if (board[1][1] == symb and board[2][2] == symb):
        num_two += 1
    #Diagonal Two
    if (board[2][0] == symb and board[1][1] == symb):
        num_two += 1
    if (board[2][0] == symb and board[0][2] == symb):
        num_two += 1
    if (board[1][1] == symb and board[0][2] == symb):
        num_two += 1
    return num_two