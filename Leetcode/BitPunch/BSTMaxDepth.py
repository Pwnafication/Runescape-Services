class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_symmetric_tree():
    # Level 3
    node7 = TreeNode(4)
    node8 = TreeNode(4)
    node5 = TreeNode(3)
    node6 = TreeNode(3)

    # Level 2
    node3 = TreeNode(2, node5, node6)
    node4 = TreeNode(2, node7, node8)

    # Level 1 (root)
    root = TreeNode(1, node3, node4)

    return root

def print_tree_preorder(node):
    if not node:
        return
    print(node.value, end=" ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

################################################################################
    

# Create the symmetric binary tree
symmetric_tree = create_symmetric_tree()

# Print the tree in preorder to confirm structure
print("Preorder traversal of the symmetric tree:")
print_tree_preorder(symmetric_tree)


def findMaxDepth(node):
    if node is None:
        return 0
    left = findMaxDepth(node.left)
    right = findMaxDepth(node.right)
    ans = max(left,right)
    return ans+1
print("")
print(findMaxDepth(symmetric_tree))