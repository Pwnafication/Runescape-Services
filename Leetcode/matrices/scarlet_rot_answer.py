from collections import deque

test_matrix = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

directions = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]

ROTTEN = 2
FRESH = 1
EMPTY = 0

def oranges_rotting(matrix):
    if len(matrix) == 0:
        return 0

    queue = deque()
    fresh_oranges = 0

    # Initialize the queue and count fresh oranges
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == ROTTEN:
                queue.append((row, col))
            if matrix[row][col] == FRESH:
                fresh_oranges += 1

    minutes = 0
    current_queue_size = len(queue)

    while queue:
        if current_queue_size == 0:
            current_queue_size = len(queue)
            minutes += 1

        current_orange = queue.popleft()
        current_queue_size -= 1
        row, col = current_orange

        for current_dir in directions:
            next_row = row + current_dir[0]
            next_col = col + current_dir[1]

            if (next_row < 0 or next_row >= len(matrix) or 
                next_col < 0 or next_col >= len(matrix[0])):
                continue

            if matrix[next_row][next_col] == FRESH:
                matrix[next_row][next_col] = ROTTEN
                fresh_oranges -= 1
                queue.append((next_row, next_col))

    if fresh_oranges != 0:
        return -1

    return minutes

print(oranges_rotting(test_matrix))
