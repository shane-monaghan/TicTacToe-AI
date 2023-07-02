from gamelogic import *

def minimize(root):

    min = root.child[0].value
    min_node = root.child[0]
    for node in root.child:
        if node.value < min:
            min = node.value
            min_node = node
    maximize(min_node)

def maximize(root):
    max = root.child[0].value
    max_node = root.child[0]
    for node in root.child:
        if node.value > max:
            max = node.value
            max_node = node
    minimize(max_node)

def eval_move(board, symb, move):
    value = 0
    if symb == 'X':
        symb_multiplier = 1
    if symb == 'O':
        symb_multiplier = -1
    if check_win(board, symb):
        value += (50 * symb_multiplier)
    if move == (0, 0) or move == (0,2) or move ==(2, 0) or move == (2, 2):
        value += (5 * symb_multiplier)
    value += num_two_in_row(board, symb) * 0.2 * symb_multiplier
    return value


