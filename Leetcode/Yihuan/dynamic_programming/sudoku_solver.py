def get_box_id(row, col):
    # Calculate the box ID for the given cell (row, col)
    # Each 3x3 box is uniquely identified by this formula
    row_val = (row // 3) * 3  # Determine the row group
    col_val = col // 3        # Determine the column group
    return row_val + col_val

def is_valid(box, row, col, num):
    # Check if the number is already present in the corresponding box, row, or column
    if num in box or num in row or num in col:
        return False  # Number placement violates Sudoku rules
    return True  # Placement is valid

def solve_backtrack(board, boxes, rows, cols, r, c):
    # Recursive function to solve the Sudoku puzzle using backtracking
    if r == len(board) or c == len(board[0]):
        # Base case: if we've reached the end of the board, the puzzle is solved
        return True
    else:
        if board[r][c] == '.':
            # If the current cell is empty, try placing numbers 1 through 9
            for num in range(1, 10):
                num_val = str(num)  # Convert number to string as board stores values as strings
                board[r][c] = num_val  # Tentatively place the number in the cell

                # Determine the corresponding box, row, and column constraints
                box_id = get_box_id(r, c)
                box = boxes[box_id]
                row = rows[r]
                col = cols[c]

                if is_valid(box, row, col, num_val):
                    # If the placement is valid, mark the number in the constraints
                    box[num_val] = True
                    row[num_val] = True
                    col[num_val] = True

                    # Move to the next cell: either next row or next column
                    if c == len(board[0]) - 1:  # End of current row
                        if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                            return True  # Continue solving recursively
                    else:  # Same row, move to next column
                        if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                            return True  # Continue solving recursively

                    # Backtrack: undo the placement and remove it from the constraints
                    del box[num_val]
                    del row[num_val]
                    del col[num_val]

                # Reset the cell if the placement doesn't lead to a solution
                board[r][c] = '.'
        else:
            # If the cell is already filled, move to the next cell
            if c == len(board[0]) - 1:  # End of current row
                if solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                    return True
            else:  # Same row, move to next column
                if solve_backtrack(board, boxes, rows, cols, r, c + 1):
                    return True

    # If no valid number can be placed, return False to backtrack
    return False

def solve_sudoku(board):
    # Initialize the constraints: one dictionary for each box, row, and column
    n = len(board)
    boxes = [{} for _ in range(n)]  # Track numbers in each 3x3 box
    rows = [{} for _ in range(n)]  # Track numbers in each row
    cols = [{} for _ in range(n)]  # Track numbers in each column

    # Prepopulate constraints with the existing numbers on the board
    for r in range(n):
        for c in range(n):
            if board[r][c] != '.':  # Skip empty cells
                box_id = get_box_id(r, c)
                val = board[r][c]
                boxes[box_id][val] = True  # Mark the number in the box
                rows[r][val] = True       # Mark the number in the row
                cols[c][val] = True       # Mark the number in the column

    # Solve the board using backtracking
    solve_backtrack(board, boxes, rows, cols, 0, 0)

# Example board
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]

# Solve the Sudoku puzzle
solve_sudoku(board)

# Display the solved Sudoku board
for row in board:
    print(row)
