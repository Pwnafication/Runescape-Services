# 230. Kth Smallest Element in a BST
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:


# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = None

        def recursNodes(node):
            if not node: 
                return None
            recursNodes(node.left)
            if self.result != None:
                return
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return 
            recursNodes(node.right)
        recursNodes(root)
        return self.result



    
#     1
#    / \
#   2   3
#  / \
# 4   5