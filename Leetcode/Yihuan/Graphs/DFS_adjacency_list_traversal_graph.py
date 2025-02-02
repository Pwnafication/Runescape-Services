adjacency_matrix = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0]
]

values = []
seen = set()
vertex = 0

def traversal_dfs(matrix,vertex,values,seen):
    values.append(vertex)
    seen.add(vertex)

    row = matrix[vertex]
    for colIndex, colValue in enumerate(row):
        if colValue == 1 and colIndex not in seen:
            traversal_dfs(matrix,colIndex,values,seen)

    return values

values = traversal_dfs(adjacency_matrix,0,values,seen)
print(values)

