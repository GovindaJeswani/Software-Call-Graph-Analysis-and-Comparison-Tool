from board import generate_board
from validator import is_valid_move
from utils import print_board
from game_logic import is_game_complete

def main():
    print("Welcome to Sudoku!")
    board = generate_board()
    
    while not is_game_complete(board):
        print_board(board)
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))
            
            if is_valid_move(board, row, col, num):
                board[row][col] = num
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
    print("Congratulations! You solved the Sudoku puzzle!")

if __name__ == "__main__":
    main()
