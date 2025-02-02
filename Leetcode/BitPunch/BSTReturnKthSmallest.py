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

class Solution:
    @staticmethod
    def findKthSmallest(node, k):
        # Helper function for in-order traversal
        def in_order_traversal(node):
            nonlocal k
            if node is None:
                return None
            
            # Traverse the left subtree
            left = in_order_traversal(node.left)
            if left is not None:
                return left
            
            # Process the current node
            k -= 1
            if k == 0:
                return node.value
            
            # Traverse the right subtree
            return in_order_traversal(node.right)
        
        # Start in-order traversal
        return in_order_traversal(node)

################################################################################

# Example usage
print("") 
k = 5
result = Solution.findKthSmallest(symmetric_tree, k)
print(f"Kth smallest element (k={k}): {result}")
