from collections import deque

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

def traversal_bfs(graph):
    seen = set()  # Set to keep track of visited nodes
    queue = deque([0])  # Start with vertex 0
    values = []  # Store traversal order

    while queue:
        vertex = queue.popleft()  # Dequeue the first vertex
        if vertex not in seen:
            values.append(vertex)  # Add the vertex to the traversal order
            seen.add(vertex)  # Mark the vertex as seen

            connections = graph[vertex]
            for v in range(len(connections)):
                if connections[v] > 0 and v not in seen:
                    queue.append(v)  # Enqueue connected vertices

    return values

# Perform BFS traversal
result = traversal_bfs(adjacency_matrix)
print(result)

