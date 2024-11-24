costs = [20, 15, 30, 5]

def minCostClimbingStairs(costs):
    n = len(costs)
    if n == 0:
        return 0
    if n == 1:
        return costs[0]
    if n == 2:
        return min(costs[0], costs[1])

    memo = [-1] * n
    memo[0] = costs[0]
    memo[1] = costs[1]

    for i in range(2, n):
        memo[i] = costs[i] + min(memo[i - 1], memo[i - 2])

    # Return the minimum cost to reach the top, which could be either from the last step or the second-to-last step
    return min(memo[n - 1], memo[n - 2])

print(minCostClimbingStairs(costs))
