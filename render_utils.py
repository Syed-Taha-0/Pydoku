import pygame

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
number_font_size = 30
title_font = pygame.font.Font("Fonts/Montserrat/static/Montserrat-Bold.ttf", 78)
number_font = pygame.font.Font(
    "Fonts/Nunito/static/Nunito-Medium.ttf", number_font_size
)
plain_text_font = pygame.font.Font("Fonts/Montserrat/static/Montserrat-Regular.ttf", 25)


def draw_board_surface(board_image, SCREEN_WIDTH, SCREEN_HEIGHT, screen):
    board_rect = board_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.75))
    screen.blit(board_image, (board_rect))


def render_title(SCREEN_WIDTH, SCREEN_HEIGHT, screen):
    title_surface = title_font.render("Pydoku", True, (216, 222, 233))
    title_surface_rect = title_surface.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 9)
    )
    screen.blit(title_surface, title_surface_rect)


def is_digit_permanent(highlight_row, highlight_column, board_matrix_permanent):
    number = board_matrix_permanent[highlight_row][highlight_column]
    if number == 0:
        return False
    else:
        return True


def render_number(
    board_matrix, screen, column_number, row_number, board_matrix_permanent
):
    number_text = None
    if board_matrix[row_number][column_number] != 0:
        if is_digit_permanent(row_number, column_number, board_matrix_permanent):
            number = board_matrix[row_number][column_number]
            number_text = number_font.render(f"{number}", True, (150, 166, 177))
            number_text_rect = number_text.get_rect(
                center=(227 + column_number * 62, 180 + row_number * 63)
            )
        else:
            number = board_matrix[row_number][column_number]
            number_text = number_font.render(f"{number}", True, (236, 239, 244))
            number_text_rect = number_text.get_rect(
                center=(227 + column_number * 62, 180 + row_number * 63)
            )
    if not number_text == None:
        screen.blit(
            number_text,
            (
                227 + column_number * 62 + number_font_size / 2,
                180 + row_number * 63 + number_font_size / 4,
            ),
        )


# render the current state of the board_matrix array on to the screen
def render_numbers(board_matrix, board_matrix_permanent, screen):
    for i in range(9):
        for j in range(9):
            render_number(board_matrix, screen, i, j, board_matrix_permanent)


# draw a highlight around the current active rectangle
# the board top left cell (x, y) are 227, 180...
# each cell is about 62 pixels apart in the x-axis
def draw_highlight_rectangle(screen, column_number, row_number):
    highlight_rect_color = [163, 190, 140]
    pygame.draw.rect(
        screen,
        highlight_rect_color,
        (227 + column_number * 62, 180 + row_number * 63, 50, 50),
        width=5,
        border_radius=12,
    )


def game_over(screen):
    game_over_title_text = title_font.render("You Won!", True, (163, 190, 140))
    game_over_rect = game_over_title_text.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.2)
    )
    add_info_text = plain_text_font.render(
        "Press ENTER to play again", True, (216, 222, 233)
    )
    add_info_text_rect = add_info_text.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.80)
    )
    screen.blit(game_over_title_text, game_over_rect)
    screen.blit(add_info_text, add_info_text_rect)
    ...
