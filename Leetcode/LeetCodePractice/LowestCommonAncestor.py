# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium
# Topics
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur = root
        while cur:
            # Compare with the values of p and q, not the nodes themselves
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left  # Go left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right  # Go right
            else:
                return cur  # Found the LCA
