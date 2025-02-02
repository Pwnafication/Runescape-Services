# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        if preorder is None and inorder is None:
            return True
        if preorder is None or inorder is None:
            return False
        
        def recurOnMainNode(self, preorder, inorder):
            if preorder is None or inorder is None:
                return None
            root = preorder[0]
            

        return self.recurOnMainNode(preorder, inorder)
        