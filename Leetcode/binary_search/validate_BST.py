class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def Validate(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if node.value <= min_val or node.value >= max_val:
        return False
    return Validate(node.left, min_val, node.value) and Validate(node.right, node.value, max_val)

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

result = Validate(root)
print(result)
