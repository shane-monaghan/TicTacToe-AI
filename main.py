from gamelogic import *
from tree import *
from ai_logic import *
def main():
    board = [['' for i in range(3)] for i in range(3)]
    has_winner = False
    '''
    while has_winner == False:
        display_board(board)
        player_move(board)
        has_winner = check_win(board, 'X')
        if has_winner:
            display_board(board)
            print('Player Wins!')
            break
    '''
    root = Node(board)
    create_tree(board, 'O', root)
    update_values(root)
    for board in root.child:
        print(board.value)
main()
