import heapq

times = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
k = 1 
N = 5


def network_delay_time(times, n, k):
    distances = [float('inf')] * n
    adj_list = [[] for _ in range(n)]
    distances[k - 1] = 0

    # Min-heap priority queue
    heap = [(0, k - 1)]  # (distance, node)

    # Build the adjacency list
    for source, target, weight in times:
        adj_list[source - 1].append((target - 1, weight))

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        # Skip if the current distance is not optimal
        if current_distance > distances[current_vertex]:
            continue

        for neighboring_vertex, weight in adj_list[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighboring_vertex]:
                distances[neighboring_vertex] = distance
                heapq.heappush(heap, (distance, neighboring_vertex))

    ans = max(distances)
    return -1 if ans == float('inf') else ans


# Test the function
print(network_delay_time(times, N, k))  # Output: Network delay time result
