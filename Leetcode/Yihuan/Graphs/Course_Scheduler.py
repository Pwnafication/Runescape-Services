# adj_list = [[1], [2], [], [0, 4], [2], []]
# in_degree = [1, 1, 2, 0, 2, 0]
# stack = [3, 5]

p = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]

def can_finish_with_adj(n, prerequisites):
    in_degree = [0] * n
    adj_list = [[] for _ in range(n)]

    for pair in prerequisites:
        in_degree[pair[0]] += 1
        adj_list[pair[1]].append(pair[0])

    stack = [i for i in range(n) if in_degree[i] == 0]

    count = 0

    while stack:
        current = stack.pop()
        count += 1

        for next_course in adj_list[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                stack.append(next_course)

    return count == n

print(can_finish_with_adj(6, p))
