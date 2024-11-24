from collections import deque

adjacency_list = [
    [1, 3],
    [0],
    [3, 8],
    [0, 2, 4, 5],
    [3, 6],
    [3],
    [4, 7],
    [6],
    [2]
]

def traversal_bfs(graph):
    queue = deque([0])  # Use deque for efficient queue operations
    values = []
    seen = set()  # Use a set to keep track of seen nodes

    while queue:
        vertex = queue.popleft()  # Dequeue the first element
        values.append(vertex)
        seen.add(vertex)

        connections = graph[vertex]
        for connection in connections:
            if connection not in seen:
                queue.append(connection)

    return values,seen

values = traversal_bfs(adjacency_list)
print(values)