def display_board(board):
    """
    Prints the board on the console

    :param board: 2D Array; represents the current state of the board
    :return: None
    """
    for row in board:
        print(row)


def player_move(board):
    """
    Gets player input in order to make a move, checks to see if it is a
    valid move before doing so

    :param board: 2D Array; represents the current state of the board
    :return: None
    """
    while True:
        row = input('Enter a row (0-2, from top to bottom)')
        col = input('Enter a column (0-2, from left to right)')
        if valid_move(board, row, col):
            board[int(row)][int(col)] = 'X'
            break


def valid_move(board, row, col):
    """
    Determines whether a move can be played or not

    :param board: 2D Array; represents the current state of the board
    :param row: int; represents the row of the move to be checked
    :param col: int; represents the column of the move to be checked
    :return: True if the move can be played, False otherwise
    """
    #if not (row.isnumeric() and col.isnumeric()):
        #return False
    row = int(row)
    col = int(col)
    valid_nums = [0, 1, 2]
    if row in valid_nums and col in valid_nums:
        if board[int(row)][int(col)] != '':
            return False
        else:
            return True


def check_win(board, symb):
    """
    This function checks every row, column, and diagonal to determine whether
    the player or AI, dependent on the symbol passed in, has won the game by
    achieving three in a row.

    :param board: 2D array; represents the current state of the board
    :param symb: String; the symbol, either an 'X' or 'O' to be checked for three in a row
    :return: True if three in a row found; False otherwise
    """
    # Check Rows
    if board[0][0] == symb and board[0][1] == symb and board[0][2] == symb:
        return True
    if board[1][0] == symb and board[1][1] == symb and board[1][2] == symb:
        return True
    if board[2][0] == symb and board[2][1] == symb and board[2][2] == symb:
        return True
    # Check Cols
    if board[0][0] == symb and board[1][0] == symb and board[2][0] == symb:
        return True
    if board[0][1] == symb and board[1][1] == symb and board[2][1] == symb:
        return True
    if board[0][2] == symb and board[1][2] == symb and board[2][2] == symb:
        return True
    # Check Diagonals
    if board[0][0] == symb and board[1][1] == symb and board[2][2] == symb:
        return True
    if board[2][0] == symb and board[1][1] == symb and board[0][2] == symb:
        return True
    return False


def num_two_in_row(board, symb):
    """
    Counts the number of rows, columns, and diagonals that have 2
    of either an 'X' or 'O' in them, dependent on what symbol is
    passed in.

    :param board: 2D Array; represents the current state of the board
    :param symb: String; the symbol that will be searched for on the board
    :return: int; the number of rows, columns, and diagonals that have 2 of a symbol
    """
    num_two = 0
    # Row One
    if board[0][0] == symb and board[0][1] == symb:
        num_two += 1
    if board[0][0] == symb and board[0][2] == symb:
        num_two += 1
    if board[0][1] == symb and board[0][2] == symb:
        num_two += 1
    # Row Two
    if board[1][0] == symb and board[1][1] == symb:
        num_two += 1
    if board[1][0] == symb and board[1][2] == symb:
        num_two += 1
    if board[1][1] == symb and board[1][2] == symb:
        num_two += 1
    # Row Three
    if board[2][0] == symb and board[2][1] == symb:
        num_two += 1
    if board[2][0] == symb and board[2][2] == symb:
        num_two += 1
    if board[2][1] == symb and board[2][2] == symb:
        num_two += 1
    # Col One
    if board[0][0] == symb and board[1][0] == symb:
        num_two += 1
    if board[0][0] == symb and board[2][0] == symb:
        num_two += 1
    if board[1][0] == symb and board[2][0] == symb:
        num_two += 1
    # Col Two
    if board[0][1] == symb and board[1][1] == symb:
        num_two += 1
    if board[0][1] == symb and board[2][1] == symb:
        num_two += 1
    if board[1][1] == symb and board[2][1] == symb:
        num_two += 1
    # Col Three
    if board[0][2] == symb and board[1][2] == symb:
        num_two += 1
    if board[0][2] == symb and board[2][2] == symb:
        num_two += 1
    if board[1][2] == symb and board[2][2] == symb:
        num_two += 1
    # Diagonal One
    if board[0][0] == symb and board[1][1] == symb:
        num_two += 1
    if board[0][0] == symb and board[2][2] == symb:
        num_two += 1
    if board[1][1] == symb and board[2][2] == symb:
        num_two += 1
    # Diagonal Two
    if board[2][0] == symb and board[1][1] == symb:
        num_two += 1
    if board[2][0] == symb and board[0][2] == symb:
        num_two += 1
    if board[1][1] == symb and board[0][2] == symb:
        num_two += 1
    return num_two
