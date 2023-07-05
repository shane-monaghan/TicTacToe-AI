import pygame
import sys
from tree import *
from ai_logic import *


def game_with_graphics():
    # Pygame Setup
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption('Tic-Tac-Toe')
    clock = pygame.time.Clock()
    # Game Variables
    board = [['' for i in range(3)] for i in range(3)]
    has_winner = False
    num_moves = 0
    result = None

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        while has_winner == False:
            draw_board(screen, board)
            pygame.display.update()
            get_click(board)
            num_moves += 1
            draw_board(screen, board)
            pygame.display.update()
            has_winner = check_win(board, 'X')
            if has_winner:
                result = 'Player'
                break
            if num_moves == 9:
                has_winner = True
                result = 'Draw'
                break
            root = Node(board, None)
            create_tree(board, root)
            make_move(root)
            num_moves += 1
            draw_board(screen, board)
            pygame.display.update()
            has_winner = check_win(board, 'O')
            if has_winner:
                result = 'Computer'
                break
        print_result(screen, board, result)
        clock.tick(60)


def draw_board(screen, board):
    screen.fill('white')
    pygame.draw.line(screen, 'black', (150, 0), (150, 450))
    pygame.draw.line(screen, 'black', (300, 0), (300, 450))
    pygame.draw.line(screen, 'black', (0, 150), (450, 150))
    pygame.draw.line(screen, 'black', (0, 300), (450, 300))

    font = pygame.font.Font('freesansbold.ttf', 64)
    x_text = font.render('X', True, 'red', 'white')
    x_rect = x_text.get_rect()
    o_text = font.render('O', True, 'blue', 'white')
    o_rect = o_text.get_rect()

    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if row_index == 0:
                y_center = 75
            elif row_index == 1:
                y_center = 225
            else:
                y_center = 375
            if col_index == 0:
                x_center = 75
            elif col_index == 1:
                x_center = 225
            else:
                x_center = 375
            if board[row_index][col_index] == 'X':
                x_rect.center = (x_center, y_center)
                screen.blit(x_text, x_rect)
            if board[row_index][col_index] == 'O':
                o_rect.center = (x_center, y_center)
                screen.blit(o_text, o_rect)


def print_result(screen, board, result):
    surface = pygame.Surface((450, 450), pygame.SRCALPHA)
    surface.fill((0, 0, 0, 128))
    font = pygame.font.Font('freesansbold.ttf', 54)
    draw_board(screen, board)
    if result == 'Player':
        player_victory_text = font.render('Player Wins!', True, 'red', 'white')
        player_victory_rect = player_victory_text.get_rect()
        player_victory_rect.center = (225, 225)
        surface.blit(player_victory_text, player_victory_rect)
    elif result == 'Computer':
        computer_victory_text = font.render('Computer Wins!', True, 'blue', 'white')
        computer_victory_rect = computer_victory_text.get_rect()
        computer_victory_rect.center = (225, 225)
        surface.blit(computer_victory_text, computer_victory_rect)
    else:
        draw_text = font.render('Game Drawn!', True, 'purple', 'white')
        draw_rect = draw_text.get_rect()
        draw_rect.center = (225, 225)
        surface.blit(draw_text, draw_rect)
    screen.blit(surface, (0, 0))
    pygame.display.update()


def get_click(board):
    pos = None
    while pos is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
    if pos[0] <= 150:
        col = 0
    elif pos[0] <= 300:
        col = 1
    elif pos[0] <= 450:
        col = 2
    if pos[1] <= 150:
        row = 0
    elif pos[1] <= 300:
        row = 1
    elif pos[1] <= 450:
        row = 2
    if valid_move(board, row, col):
        board[int(row)][int(col)] = 'X'
    else:
        get_click(board)