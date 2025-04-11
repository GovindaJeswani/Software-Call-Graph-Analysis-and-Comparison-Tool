def is_game_complete(board):
    """
    Check if the Sudoku board is completely and correctly solved.
    """
    # Check if there are any empty cells
    for row in board:
        if 0 in row:
            return False

    # Check rows and columns
    for i in range(9):
        if not is_valid_group([board[i][j] for j in range(9)]):  # Check row
            return False
        if not is_valid_group([board[j][i] for j in range(9)]):  # Check column
            return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [
                board[row + i][col + j]
                for i in range(3)
                for j in range(3)
            ]
            if not is_valid_group(subgrid):
                return False

    return True


def is_valid_group(group):
    """
    Check if a group (row, column, or subgrid) contains all numbers from 1 to 9 exactly once.
    """
    return sorted(group) == list(range(1, 10))
