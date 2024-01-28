import random

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def display_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
    print()

def merge_tiles(row):
    new_row = [0] * 4
    index = 0
    for tile in row:
        if tile != 0:
            if new_row[index] == 0:
                new_row[index] = tile
            elif new_row[index] == tile:
                new_row[index] *= 2
                index += 1
            else:
                index += 1
                new_row[index] = tile
    return new_row

def transpose_board(board):
    return [list(row) for row in zip(*board)]

def move_left(board):
    new_board = []
    for row in board:
        new_row = merge_tiles(row)
        new_board.append(new_row)
    return new_board

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    new_board = []
    for row in reversed_board:
        new_row = merge_tiles(row)
        new_board.append(new_row[::-1])
    return new_board

def move_up(board):
    transposed_board = transpose_board(board)
    new_board = move_left(transposed_board)
    return transpose_board(new_board)

def move_down(board):
    transposed_board = transpose_board(board)
    new_board = move_right(transposed_board)
    return transpose_board(new_board)

def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
        for i in range(3):
            if row[i] == row[i + 1]:
                return False
    return True