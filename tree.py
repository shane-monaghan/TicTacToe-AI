import copy
from ai_logic import *
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.value = None

    def add_child(self, node):
        self.child += [node]

def create_tree(board, symb, node):
    list_moves = possible_moves(board)
    for move in list_moves:
        copy_board = copy.deepcopy(board)
        copy_board[move[0]][move[1]] = symb
        value = eval_move(copy_board, symb, move)
        new_node = Node(copy_board)
        new_node.value = value
        node.add_child(new_node)
        if symb == 'X':
            create_tree(copy_board, 'O', new_node)
        else:
            create_tree(copy_board, 'X', new_node)

def update_values(root):
    update_values_helper(root)

def update_values_helper(root):
    if root != None:
        for node in root.child:
            update_values_helper(node)
            if node.value != None and root.value != None:
                root.value += node.value


def possible_moves(board):
    list_moves = []
    for row_index in range(len(board)):
        for col_index in range(len(board)):
            if board[row_index][col_index] == '':
                list_moves += [(row_index, col_index)]
    return list_moves
