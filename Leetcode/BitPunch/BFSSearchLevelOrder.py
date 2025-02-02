from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Create a 5-level tree
def create_5_level_tree():
    # Level 5
    node15 = TreeNode(15)
    node16 = TreeNode(16)
    node17 = TreeNode(17)
    node18 = TreeNode(18)
    node19 = TreeNode(19)
    node20 = TreeNode(20)
    node21 = TreeNode(21)
    node22 = TreeNode(22)
    
    # Level 4
    node9 = TreeNode(9, node15, node16)
    node10 = TreeNode(10, node17, node18)
    node11 = TreeNode(11, node19, node20)
    node12 = TreeNode(12, node21, node22)
    
    # Level 3
    node5 = TreeNode(5, node9, node10)
    node6 = TreeNode(6, node11, node12)
    
    # Level 2
    node3 = TreeNode(3, node5, None)
    node4 = TreeNode(4, None, node6)
    
    # Level 1 (Root)
    root = TreeNode(1, node3, node4)
    
    return root

# BFS traversal that returns levels as lists
def bfs_levels(root: TreeNode):
    if not root:
        return None
    
    theBigList = []  # Stores the final level order traversal result
    TheMainQueue = deque([root])  # Queue for nodes in the current level, initialized as a deque

    while TheMainQueue:
        nextLevelNodesQueue = deque()  # Queue for nodes in the next level (also a deque now)
        currentLevelValues = []  # Values of nodes in the current level
        for i in range(len(TheMainQueue)):
            node = TheMainQueue.popleft()  # Use deque's popleft for O(1) performance
            currentLevelValues.append(node.value)
            if node.left:
                nextLevelNodesQueue.append(node.left)  # Add left child to the next level queue
            if node.right:
                nextLevelNodesQueue.append(node.right)  # Add right child to the next level queue
        theBigList.append(currentLevelValues)
        TheMainQueue = nextLevelNodesQueue  # Move to the next level

    return theBigList


# Create the tree
root = create_5_level_tree()

# Perform BFS and print the levels
levels = bfs_levels(root)
print("BFS Levels:")
for levelIndex, level in enumerate(levels, start=1):
    print(f"Level {levelIndex}: {level}")
