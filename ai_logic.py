from gamelogic import *
from sys import maxsize
def minimize(root):
    if len(root.child) == 0:
        return None, root.value
    min = maxsize
    min_move = None
    for node in root.child:
        move, eval = maximize(node)
        if node.value < min:
            min = node.value
            min_move = node
    return min_move, min


def maximize(root):
    max = maxsize * -1
    max_move = None
    for node in root.child:
        move, eval = minimize(node)
        if node.value > max:
            max = node.value
            max_move = node
    return max_move, max

def eval_move(board, symb, move):
    value = 0
    if symb == 'X':
        symb_multiplier = 1
    if symb == 'O':
        symb_multiplier = -1
    if check_win(board, symb):
        value += (50 * symb_multiplier)
    if move == (0, 0) or move == (0,2) or move ==(2, 0) or move == (2, 2):
    #if board[0][0] == symb or board[0][2] == symb or board[2][0] == symb or board[2][2] == symb:
        value += (3 * symb_multiplier)
    value += num_two_in_row(board, symb) * 5 * symb_multiplier
    return value

def make_move(board):
    node, eval = minimize(board)
    move = node.move
    board.data[move[0]][move[1]] = 'O'


