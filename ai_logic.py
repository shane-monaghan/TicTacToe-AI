from gamelogic import *
from sys import maxsize
import random
def minimize(root):
    if len(root.child) == 0:
        return None, root.value
    min = maxsize
    min_move = []
    for node in root.child:
        maximize(node)
        if node.value < min:
            min = node.value
            root.value = min
            min_move = [node]
        elif node.value == min:
            min_move += [node]
    return min_move, min
def maximize(root):
    max = maxsize * -1
    max_move = []
    for node in root.child:
        minimize(node)
        if node.value > max:
            max = node.value
            root.value = max
            max_move = [node]
        elif node.value == max:
            max_move += [node]
    return max_move, max
def eval_move(board, symb, move):
    value = 0
    symb_mult_x = 1
    symb_mult_o = -1
    if check_win(board, 'X'):
        value += (50 * symb_mult_x)
    if check_win(board, 'O'):
        value += (50 * symb_mult_o)
    #if move == (0, 0) or move == (0,2) or move ==(2, 0) or move == (2, 2):
    if board[0][0] == 'X' or board[0][2] == 'X' or board[2][0] == 'X' or board[2][2] == 'X':
        value += (3 * symb_mult_x)
    if board[0][0] == 'O' or board[0][2] == 'O' or board[2][0] == 'O' or board[2][2] == 'O':
        value += (3 * symb_mult_o)
    value += num_two_in_row(board, 'X') * 5 * symb_mult_x
    value += num_two_in_row(board, 'O') * 5 * symb_mult_o
    return value
def make_move(board):
    node_list, eval = minimize(board)
    node = random.choice(node_list)
    move = node.move
    board.data[move[0]][move[1]] = 'O'


