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

def isValid(row, columm, box, num):
    if num in row or num in columm or num in box:
        return False
    return True

def get_box_id(row, col):
    col_index = (col // 3)
    row_index = (row // 3) * 3
    return col_index + row_index

def sudoku_recursion(box, rows, cols, num):

def construct_and_solve(board):
    n = len(board)
    box =  [{} for each in range(n)]
    rows = [{} for each in range(n)]
    cols = [{} for each in range(n)]

    for row in range(n):
        for col in range(n):
            value = board[row][col]
            if value != '.':
                box_index = get_box_id(row,col)
                box[box_index][value] = True
                rows[row][value] = True
                cols[col][value] = True
    sudoku_recursion()
    