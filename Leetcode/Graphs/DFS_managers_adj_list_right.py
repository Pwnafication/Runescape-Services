managersArray = [2, 2, 4, 6, -1, 4, 4, 5]
informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0]

# Step 1: Build the adjacency list
adjList = [[] for _ in range(len(managersArray))]
for employeeIndex, managerValue in enumerate(managersArray):
    if managerValue != -1:
        adjList[managerValue].append(employeeIndex)

# Step 2: Define the DFS function
def dfs(node, cumulativeTime):
    # Base case: If this node has no subordinates, return cumulativeTime
    if not adjList[node]:
        return cumulativeTime
    
    # Recursive case: Traverse all subordinates
    maxTime = 0
    for subordinate in adjList[node]:
        maxTime = max(maxTime, dfs(subordinate, cumulativeTime + informTimeArray[node]))
    
    return maxTime

# Step 3: Find the root (manager with -1) and start DFS
root = managersArray.index(-1)
totalTime = dfs(root, 0)

print(totalTime)  # Output: 13
