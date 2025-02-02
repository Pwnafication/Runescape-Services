class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth(node, currentDepth=1):
    if node is None:
        return currentDepth - 1
    currentDepth += 1
    return max(max_depth(node.left, currentDepth), max_depth(node.right, currentDepth))

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

depth = max_depth(root)
print(depth)  # Should return 3
