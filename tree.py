import copy
from ai_logic import *
from gamelogic import check_win


class Node:
    def __init__(self, data, move):
        """
        The constructor for a tree Node

        :param data: 2D Array; represents the board
        :param move: Tuple; represents the move made to get to the board stored in data
        """
        self.data = data
        self.child = []
        self.move = move
        self.value = None

    def add_child(self, node):
        """
        Adds a node to the list of this node's children

        :param node: Node
        :return: None
        """
        self.child += [node]


def create_tree(board, root, symb='O'):
    """
    Creates a tree structure that has nodes containing the state
    of the board after all possible moves.

    :param board: 2D Array; represents the current state of the board
    :param symb: String; defaults to 'O' because this function is only called right before the AI moves
    :param root: Node; the node whose data represents the current state of the board
    :return: None
    """
    list_moves = possible_moves(board)
    for move in list_moves:
        copy_board = copy.deepcopy(board)
        copy_board[move[0]][move[1]] = symb
        value = eval_move(copy_board)
        new_node = Node(copy_board, move)
        new_node.value = value
        root.add_child(new_node)
        if check_win(new_node.data, symb):
            pass
        elif symb == 'X':
            create_tree(copy_board, new_node)
        else:
            create_tree(copy_board, new_node, 'X')


def possible_moves(board):
    """
    Takes in a board and returns a list of all possible moves that can be made on that board.

    :param board: 2D Array; represents the current state of the board
    :return: List of Tuples; contains all possible moves
    """
    list_moves = []
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            if board[row_index][col_index] == '':
                list_moves += [(row_index, col_index)]
    return list_moves
