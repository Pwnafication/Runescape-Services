# 98. Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        
        if not root:
            return True
        
        def validationRecursion(node, min_value, max_value):
            if not node:
                return True
            if min_value is not None and node.val <= min_value:
                    return False
            if max_value is not None and node.val >= max_value:
                    return False
                
            left = validationRecursion(node.left, min_value, node.val)
            right = validationRecursion(node.right, node.val, max_value)

            return left and right

            

        return validationRecursion(root, None, None)
        
#       7 
#   3       9 
# 1   4   8  10
# 
