managers_array = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

def num_of_minutes(n, head_id, managers, inform_time):
    # Create adjacency list
    adj_list = [[] for _ in range(n)]
    
    for employee in range(n):
        manager = managers[employee]
        if manager == -1:
            continue
        adj_list[manager].append(employee)
    
    return dfs(head_id, adj_list, inform_time)

def dfs(current_id, adj_list, inform_time):
    # Base case: If there are no subordinates, return 0
    if not adj_list[current_id]:
        return 0
    
    max_time = 0
    # Traverse subordinates
    for subordinate in adj_list[current_id]:
        max_time = max(max_time, dfs(subordinate, adj_list, inform_time))
    
    return max_time + inform_time[current_id]

# Test the function
print(num_of_minutes(8, 4, managers_array, inform_time_array))
