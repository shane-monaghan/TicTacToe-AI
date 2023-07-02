from gamelogic import *
from tree import *
from ai_logic import *
def main():
    board = [['' for i in range(3)] for i in range(3)]
    has_winner = False
    num_moves = 0
    while has_winner == False:
        display_board(board)
        player_move(board)
        num_moves += 1
        has_winner = check_win(board, 'X')
        if has_winner:
            display_board(board)
            print('Player Wins!')
            break
        if num_moves == 9:
            print('Game Drawn!')
            break
        root = Node(board, None)
        create_tree(board, 'O', root)
        make_move(root)
        num_moves += 1
        has_winner = check_win(board, 'O')
        if has_winner:
            display_board(board)
            print('Computer Wins!')
            break
main()
