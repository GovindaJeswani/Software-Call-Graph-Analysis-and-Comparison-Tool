def is_valid_move(board, row, col, num):
    # Check if the number is already in the row
    if num in board[row]:
        return False
    
    # Check if the number is already in the column
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Check if the number is in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True
