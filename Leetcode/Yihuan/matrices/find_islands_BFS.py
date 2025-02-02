from collections import deque

test_matrix = [
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1]
]

directions = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]

def number_of_islands(matrix):
    if len(matrix) == 0:
        return 0
    
    island_count = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                island_count += 1
                matrix[row][col] = 0
                queue = deque()
                queue.append((row, col))

                while queue:
                    current_row, current_col = queue.popleft()

                    for direction in directions:
                        next_row = current_row + direction[0]
                        next_col = current_col + direction[1]

                        if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
                            continue

                        if matrix[next_row][next_col] == 1:
                            queue.append((next_row, next_col))
                            matrix[next_row][next_col] = 0
                            
    return island_count

# Test the function
print(number_of_islands(test_matrix))
