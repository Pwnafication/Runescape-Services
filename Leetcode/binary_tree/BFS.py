from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def breadth_first_traversal(node):
    values = []
    queue = deque([node])
    
    while queue:
        current_node = queue.popleft()
        values.append(current_node.value)
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return values

# Creating a binary search tree for the example
#       10
#      /   \
#     5     15
#    / \   /  \
#   3   7 12  18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Perform breadth-first traversal
values = breadth_first_traversal(root)
print(values)  # Expected Output: [10, 5, 15, 3, 7, 12, 18]
