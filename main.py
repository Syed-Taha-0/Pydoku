import sys
import pygame
import sudokum

# improved version of the "check" function found in the sudokum module
import check_function
from render_utils import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Set the window preferences and stuff..
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pydoku")
game_favicon = pygame.image.load("Art/favicon.png")
pygame.display.set_icon(game_favicon)


# import Board Image
board_image = pygame.image.load("Art/board.png")

# import font:
title_font = pygame.font.Font("Fonts/Montserrat-Bold.ttf", 78)

# MAIN Board GRID creation
DIFFICULTY = 0.2
# permanent matrix in order to refer to it, to test if a digit is default or was entered by the player
board_matrix_permanent = sudokum.generate(mask_rate=DIFFICULTY)
board_matrix = [[0 for x in range(9)] for y in range(9)]

# copying over the permanent matrix into the main one that will be changed by the player
def generate_copy_board():
    for row in range(9):
        for column in range(9):
            board_matrix[row][column] = board_matrix_permanent[row][column]


generate_copy_board()

number_dict = {
    pygame.K_0: 0,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
    pygame.K_7: 7,
    pygame.K_8: 8,
    pygame.K_9: 9,
    pygame.K_KP0: 0,
    pygame.K_KP1: 1,
    pygame.K_KP2: 2,
    pygame.K_KP3: 3,
    pygame.K_KP4: 4,
    pygame.K_KP5: 5,
    pygame.K_KP6: 6,
    pygame.K_KP7: 7,
    pygame.K_KP8: 8,
    pygame.K_KP9: 9,
}

# Drawing variables SECTION:
board_imagex = 100
board_imagey = 100
highlight_column = 0
highlight_row = 0
is_solved = False

# Main game loop!
while True:
    screen.fill((46, 52, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if not is_solved:

            # Key input check system
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    highlight_column += 1
                    if highlight_column >= 9:
                        highlight_column = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    highlight_column -= 1
                    if highlight_column < 0:
                        highlight_column = 8
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    highlight_row -= 1
                    if highlight_row < 0:
                        highlight_row = 8
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    highlight_row += 1
                    if highlight_row >= 9:
                        highlight_row = 0

                if event.key in number_dict.keys():
                    is_permanent = is_digit_permanent(
                        highlight_row, highlight_column, board_matrix_permanent
                    )
                    if not is_permanent:
                        board_matrix[highlight_row][highlight_column] = number_dict[
                            event.key
                        ]
                if event.key == pygame.K_BACKSPACE:
                    is_permanent = is_digit_permanent(
                        highlight_row, highlight_column, board_matrix_permanent
                    )
                    if not is_permanent:
                        board_matrix[highlight_row][highlight_column] = 0

                is_solved = check_function.check(board_matrix)[0]
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    board_matrix_permanent = sudokum.generate(mask_rate=DIFFICULTY)
                    generate_copy_board()
                    is_solved = False

    # Function to draw the game elements:
    if not is_solved:
        draw_board_surface(board_image, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
        render_title(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
        draw_highlight_rectangle(screen, highlight_column, highlight_row)
        render_numbers(board_matrix, board_matrix_permanent, screen)
    else:
        game_over(screen)
    pygame.display.update()
