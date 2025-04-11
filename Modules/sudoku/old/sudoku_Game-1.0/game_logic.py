def is_game_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True
