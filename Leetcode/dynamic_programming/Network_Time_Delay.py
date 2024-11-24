import heapq

# adjList = [
# 1 ->  [(1, 9), (3, 2)],
# 2 ->  [(4, 1)],
# 3 ->  [(1, 3), (0, 5)],
# 4 ->  [(1, 4), (4, 6)],
# 5 ->  [(2, 7)]
# ]

# distances = [
#  1   INF,
#  2   INF,
#  3   INF,
#  4   INF,
#  5   INF
# ]

# heap = [
#     (0,0)
# ]

times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
k = 1 
n = 5

def network_delay_time(times, n, k):
    distances = [float('inf')] * n
    adjList = [[] for _ in range(n)]
    distances[k - 1] = 0

    heap = [(0, k-1)]

    for source,target,weight in times:
        adjList[source -1].append((target-1,weight))

    while heap: 
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance < distances[current_vertex]:
            continue

        for neighboring_vertex, weight in adjList[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighboring_vertex]:
                distances[neighboring_vertex] = distance
                heapq.heappush(heap, (distance,neighboring_vertex))

    ans = max(distances)
    return -1 if ans == float('inf') else ans

# Test the function
print(network_delay_time(times, n, k))  # Output: Network delay time result
