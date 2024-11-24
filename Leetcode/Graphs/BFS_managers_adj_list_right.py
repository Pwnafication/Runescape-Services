from collections import deque

managersArray = [2, 2, 4, 6, -1, 4, 4, 5]
informTimeArray = [0, 0, 4, 0, 7, 3, 6, 0]

# Step 1: Build the adjacency list
adjList = [[] for _ in range(len(managersArray))]

for employeeIndex, managerValue in enumerate(managersArray):
    if managerValue != -1:
        adjList[managerValue].append(employeeIndex)

# BFS traversal to calculate the maximum inform time
def traversal_bfs(adjList):
    # Find the root (the node with no manager)
    root = managersArray.index(-1)
    maxTime = 0
    
    # Queue for BFS (holds tuples of (employee, cumulative time))
    queue = deque([(root, 0)])  
    
    while queue:
        employee, cumulativeTime = queue.popleft()
        maxTime = max(maxTime, cumulativeTime)  # Update maximum time
        
        # Traverse subordinates and update their cumulative time
        for subordinate in adjList[employee]:
            queue.append((subordinate, cumulativeTime + informTimeArray[employee]))
    
    return maxTime

print("Adjacency List:", adjList)
print("Maximum Inform Time:", traversal_bfs(adjList))
