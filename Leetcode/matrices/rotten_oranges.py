from collections import deque

test_matrix = [
    [2, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1]
]

directions = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

ROTTEN = 2
FRESH = 1
EMPTY = 0



def scarlet_rot(matrix):
    if len(matrix) == 0:
        return 0

    fresh_count = 0
    queue = deque()
    
    for eachRow in range(len(matrix)):
        for eachColumn in range(len(matrix[0])):
            if matrix[eachRow][eachColumn] == ROTTEN:
                queue.append((eachRow,eachColumn))
            if matrix[eachRow][eachColumn] == FRESH:
                fresh_count +=1

    minutes = 0

    while queue and fresh_count > 0:
        for eachRot in range(len(queue)):
            rotten_tarnished = queue.popleft()
            for eachDirection in directions:
                newRow = rotten_tarnished[0] + eachDirection[0]
                newColumn = rotten_tarnished[1] + eachDirection[1]
                print(newRow,newColumn)
                if newRow < 0 or newRow >= len(matrix) or newColumn < 0 or newColumn >= len(matrix[0]):
                    continue
                
                if matrix[newRow][newColumn] == FRESH:
                    matrix[newRow][newColumn] = ROTTEN
                    fresh_count -= 1 
                    queue.append((newRow,newColumn))
        minutes +=1


    return queue,fresh_count,minutes






print(scarlet_rot(test_matrix))
