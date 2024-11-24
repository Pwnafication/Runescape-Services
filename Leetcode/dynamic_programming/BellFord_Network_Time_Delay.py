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

times = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]

def network_delay_time(times, n, k):
    distances = [float('inf')] * n
    distances[k - 1] = 0

    for _ in range(n - 1):  # Relax edges up to N-1 times
        count = 0
        for source, target, weight in times:
            if distances[source - 1] + weight < distances[target - 1]:
                distances[target - 1] = distances[source - 1] + weight
                count += 1

        if count == 0:  # Early exit if no updates were made
            break

    ans = max(distances)
    return -1 if ans == float('inf') else ans


# Example usage
print(network_delay_time(times, 5, 1))

