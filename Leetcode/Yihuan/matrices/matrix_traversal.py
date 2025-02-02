testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
]

# Directions for moving up, right, down, and left
directions = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]

def traversalDFS(matrix):
    # Initialize a "seen" matrix to track visited cells
    seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    values = []

    # Start DFS from the top-left corner of the matrix
    dfs(matrix, 0, 0, seen, values)

    return values

def dfs(matrix, row, col, seen, values):
    # Check bounds and if the cell is already seen
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or seen[row][col]:
        return
    
    # Mark the cell as seen and add its value to the values list
    seen[row][col] = True
    values.append(matrix[row][col])

    # Traverse in all four directions
    for direction in directions:
        dfs(matrix, row + direction[0], col + direction[1], seen, values)

print(traversalDFS(testMatrix))