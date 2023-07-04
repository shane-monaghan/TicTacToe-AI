from gamelogic import *
from sys import maxsize
import random


def minimize(root):
    """
    Works in conjunction with maximize(), as a part of a minimax algorithm,
    to determine the best move the AI can make

    :param root: Node; the data in this node has the current state of the board
    :return: min_move (Tuple), min_val (Float); returns the min eval of the board and the move that achieves it
    """
    if len(root.child) == 0:
        return None, root.value
    min_val = maxsize
    min_move = []
    for node in root.child:
        maximize(node)
        if node.value < min_val:
            min_val = node.value
            root.value = min_val
            min_move = [node]
        elif node.value == min_val:
            min_move += [node]
    return min_move, min_val


def maximize(root):
    """
    Works in conjunction with maximize(), as a part of a minimax algorithm,
    to determine the best move the AI can make

    :param root: Node; the data in this node has the current state of the board
    :return: max_move (Tuple), max_val (Float); returns the max eval of the board and the move that achieves it
    """
    max_val = maxsize * -1
    max_move = []
    for node in root.child:
        minimize(node)
        if node.value > max_val:
            max_val = node.value
            root.value = max_val
            max_move = [node]
        elif node.value == max_val:
            max_move += [node]
    return max_move, max_val


def eval_move(board):
    """
    Calculates a score based on the current state of the board
    - A higher score means the board is better for the player
    - A lower score means the board is better for the AI

    :param board: a 2D array; represents the board
    :return: int; represents the evaluation of the board
    """
    value = 0
    symb_mult_x = 1
    symb_mult_o = -1
    if check_win(board, 'X'):
        value += (50 * symb_mult_x)
    if check_win(board, 'O'):
        value += (50 * symb_mult_o)
    # Checks the corners of the board
    if board[0][0] == 'X' or board[0][2] == 'X' or board[2][0] == 'X' or board[2][2] == 'X':
        value += (3 * symb_mult_x)
    # Checks the corners of the board
    if board[0][0] == 'O' or board[0][2] == 'O' or board[2][0] == 'O' or board[2][2] == 'O':
        value += (3 * symb_mult_o)
    value += num_two_in_row(board, 'X') * 5 * symb_mult_x
    value += num_two_in_row(board, 'O') * 5 * symb_mult_o
    return value


def make_move(board_node):
    """
    Makes the move returned by minimize()

    :param board_node: Node; the node's data contains the current board
    :return: None
    """
    node_list, board_eval = minimize(board_node)
    node = random.choice(node_list)
    move = node.move
    board_node.data[move[0]][move[1]] = 'O'
