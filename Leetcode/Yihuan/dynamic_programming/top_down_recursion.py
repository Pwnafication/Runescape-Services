def min_cost_climbing_stairs(costs):
    n = len(costs)
    return min(min_cost(n - 1, costs), min_cost(n - 2, costs))

def min_cost(i, costs):
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return costs[i]
    return costs[i] + min(min_cost(i - 1, costs), min_cost(i - 2, costs))

print(min_cost_climbing_stairs([20, 15, 30, 5]))