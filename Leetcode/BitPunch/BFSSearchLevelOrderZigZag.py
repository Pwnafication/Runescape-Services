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

################################################################################################

from collections import deque
# BFS traversal that returns levels as lists
def bfs_levels(root: TreeNode):
    if not root:
        return None
    
    result = []
    level_queue = deque([root])
    switch = 0

    while level_queue:
        currentLevelQueue = []    
        for eachLevelNode in range(len(level_queue)):
            if switch == 0:
                node = level_queue.popleft()
                currentLevelQueue.append(node.value)
                if node.left:
                    level_queue.append(node.left)
                if node.right:
                    level_queue.append(node.right)
            else:
                node = level_queue.pop()
                currentLevelQueue.append(node.value)
                if node.right:
                    level_queue.appendleft(node.right)
                if node.left:
                    level_queue.appendleft(node.left)

        result.append(currentLevelQueue)

        switch = 1 - switch

    return result


# Create the tree
root = create_5_level_tree()

# Perform BFS and print the levels
levels = bfs_levels(root)
print("BFS Levels:")
for level in levels:
    print(level)
