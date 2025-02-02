class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_symmetric_tree(): 
    # Level 3 
    node7 = TreeNode(12) 
    node8 = TreeNode(14) 
    node5 = TreeNode(1) 
    node6 = TreeNode(3) 

    # Level 2 
    node3 = TreeNode(2, node5, node6)  # Left subtree of root 
    node4 = TreeNode(13, node7, node8)  # Right subtree of root 

    # Level 1 (root) 
    root = TreeNode(10, node3, node4)  # Root of the BST 

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

def findLowestCommonAncestor(node, t1, t2): 
    if node is None:
        return None

    # If the current node matches either t1 or t2, return it
    if node.value == t1 or node.value == t2: 
        return node
    
    # Recur for the left and right subtrees
    left = findLowestCommonAncestor(node.left, t1, t2) 
    right = findLowestCommonAncestor(node.right, t1, t2) 

    # If both sides return non-null, this node is the LCA
    if left and right:
        return node
    
    # Otherwise, return the non-null child (could be the LCA)
    return left if left else right
 
print("") 
lca = findLowestCommonAncestor(symmetric_tree, t1=14, t2=3)
print(f"Lowest Common Ancestor: {lca.value if lca else None}")
