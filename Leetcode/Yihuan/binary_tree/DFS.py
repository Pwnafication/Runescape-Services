class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(node, values):
    if node.left:
        in_order_traversal(node.left, values)
    values.append(node.value)
    if node.right:
        in_order_traversal(node.right, values)
    return values

def pre_order_traversal(node, values):
    values.append(node.value)
    if node.left:
        pre_order_traversal(node.left, values)
    if node.right:
        pre_order_traversal(node.right, values)
    return values

def post_order_traversal(node, values):
    if node.left:
        post_order_traversal(node.left, values)
    if node.right:
        post_order_traversal(node.right, values)
    values.append(node.value)
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

# Perform in-order traversal
values = []
post_order_traversal(root, values)
print(values)  # Expected Output for in_order: [3, 5, 7, 10, 12, 15, 18]
