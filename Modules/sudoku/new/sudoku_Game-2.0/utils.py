import pygame

def render_board(screen, board, selected_cell):
    for row in range(9):
        for col in range(9):
            x, y = col * 60, row * 60
            pygame.draw.rect(screen, (200, 200, 200), (x, y, 60, 60), 1)
            if board[row][col] != 0:
                font = pygame.font.Font(None, 40)
                text = font.render(str(board[row][col]), True, (0, 0, 0))
                screen.blit(text, (x + 20, y + 10))
    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(screen, (0, 0, 255), (col * 60, row * 60, 60, 60), 3)

def get_cell_from_mouse(pos):
    x, y = pos
    return y // 60, x // 60

def draw_text(screen, text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
