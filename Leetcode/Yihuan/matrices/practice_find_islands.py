from collections import deque

testMatrix = [
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1]
]


# Directions for moving up, right, down, and left
directions = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
]


def traverse_matrix(matrix):
    if len(matrix) == 0:
        return 0
    
    island_count = 0

    for eachRow in range(len(matrix)): 
        for eachCol in range(len(matrix[0])):
            if matrix[eachRow][eachCol] == 1:
                island_count += 1 
                queue = deque()
                queue.append([eachRow,eachCol])
                matrix[eachRow][eachCol] = 0

                while queue:
                    currentRow,currentCol = queue.popleft()
                    for eachDirection in directions:
                        nextRow = currentRow+eachDirection[0]
                        nextCol = currentCol+eachDirection[1]

                        if nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[0]):
                            continue

                        if matrix[nextRow][nextCol] == 1:
                            queue.append([nextRow,nextCol])
                            matrix[nextRow][nextCol] = 0
                        
    return island_count

# Test the function
print(traverse_matrix(testMatrix))