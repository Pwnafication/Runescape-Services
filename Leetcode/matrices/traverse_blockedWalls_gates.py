import math

INF = 2147483647

test_matrix = [
    [INF, -1, 0, INF],
    [INF, INF, INF, 0],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

WALL = -1
GATE = 0
EMPTY = INF
directions = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
]

def dfs(searchMatrix, row, column, count):
    if (
        row < 0 or row >= len(searchMatrix) or 
        column < 0 or column >= len(searchMatrix[0]) or 
        searchMatrix[row][column] < count   
        ):
        return

    searchMatrix[row][column] = count
    
    for eachDirection in directions:
        nextRow = row + eachDirection[0]
        nextCol = column + eachDirection[1]
        dfs(searchMatrix,nextRow,nextCol,count+1)
    
def walls_and_gates(theMatrix):
    for eachRow in range(len(theMatrix)):
        for eachCol in range(len(theMatrix[0])):
            if theMatrix[eachRow][eachCol] == GATE:
                dfs(theMatrix,eachRow,eachCol,count=0)

    

walls_and_gates(test_matrix)

for row in test_matrix:
    print(row)
