import pygame
from board import generate_board
from validator import is_valid_move
from utils import render_board, get_cell_from_mouse, draw_text
from game_logic import is_game_complete
from high_scores import save_high_score, load_high_scores
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 540, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Fonts
FONT = pygame.font.Font(None, 40)

def main():
    board = generate_board()
    selected_cell = None
    start_time = time.time()
    running = True

    while running:
        screen.fill(WHITE)
        render_board(screen, board, selected_cell)

        # Display elapsed time
        elapsed_time = int(time.time() - start_time)
        draw_text(screen, f"Time: {elapsed_time}s", 20, 550, FONT, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_cell = get_cell_from_mouse(event.pos)

            if event.type == pygame.KEYDOWN and selected_cell:
                row, col = selected_cell
                if event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9
                else:
                    num = None

                if num and is_valid_move(board, row, col, num):
                    board[row][col] = num

        if is_game_complete(board):
            elapsed_time = int(time.time() - start_time)
            draw_text(screen, "You Win!", WIDTH // 2, HEIGHT // 2, FONT, BLUE)
            pygame.display.flip()
            pygame.time.wait(2000)

            # Save high score
            player_name = input("Enter your name: ")
            save_high_score(player_name, elapsed_time)
            print("High Scores:")
            for name, score in load_high_scores():
                print(f"{name}: {score} seconds")
            running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
