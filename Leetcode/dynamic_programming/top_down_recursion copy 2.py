def min_cost_climbing_stairs(costs_list):
    n = len(costs_list)
    memo = [-1] * n
    return min(min_cost(n-1,costs_list,memo),min_cost(n-2,costs_list,memo))

def min_cost(stair_index,costs_list,memo):
    if stair_index < 0:
        return 0
    if stair_index == 1 or stair_index == 0:
        return costs_list[stair_index]
    if memo[stair_index] > -1:
        return memo[stair_index]
    memo[stair_index] = costs_list[stair_index] + min(min_cost(stair_index-1,costs_list,memo),min_cost(stair_index-2,costs_list,memo))
    return memo[stair_index]

print(min_cost_climbing_stairs([20, 15, 30, 5]))