board = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l']
]

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

rows_n = len(board)
cols_n = len(board[0])
target = "aef"

def findLetter(targetLetter, board, num_rows, num_cols, start_coord):
    row, col = start_coord

    # Check if out of bounds
    if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
        return False

    # Check if current cell matches the target letter
    if board[row][col] == targetLetter:
        return True

    # Explore all valid directions
    for direction in directions.values():
        new_row, new_col = row + direction[0], col + direction[1]
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if board[new_row][new_col] == targetLetter:
                return True

    return False

def checkMain(target, board, num_rows, num_cols):
    current_coord = (0, 0)  # Start from the top-left corner
    for letter in target:
        if not findLetter(letter, board, num_rows, num_cols, current_coord):
            return False
    return True

print(checkMain(target, board, rows_n, cols_n))
