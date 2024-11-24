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

def scarlet_rot(matrix):
    fresh_count = 0
    queue = deque()

    # Initialize queue with all rotten oranges and count fresh ones
    for eachRow in range(len(matrix)):
        for eachColumn in range(len(matrix[0])):
            if matrix[eachRow][eachColumn] == ROTTEN:
                queue.append((eachRow, eachColumn))
            if matrix[eachRow][eachColumn] == FRESH:
                fresh_count += 1

    minutes = 0

    # Perform BFS
    while queue and fresh_count > 0:
        for _ in range(len(queue)):  # Process all rotten oranges at the current "minute"
            rotten_tarnished = queue.popleft()
            for eachDirection in directions:
                newRow = rotten_tarnished[0] + eachDirection[0]
                newColumn = rotten_tarnished[1] + eachDirection[1]
                
                # Check bounds and if the orange is fresh
                if newRow < 0 or newRow >= len(matrix) or newColumn < 0 or newColumn >= len(matrix[0]):
                    continue
                
                if matrix[newRow][newColumn] == FRESH:
                    matrix[newRow][newColumn] = ROTTEN
                    fresh_count -= 1
                    queue.append((newRow, newColumn))
        minutes += 1  # Increment minutes after processing the current level of BFS

    return -1 if fresh_count > 0 else minutes

print(scarlet_rot(test_matrix))
