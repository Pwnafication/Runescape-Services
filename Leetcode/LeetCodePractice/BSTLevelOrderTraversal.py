# 102. Binary Tree Level Order Traversal
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the level order traversal of its nodes' vals. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []

#     1
#    / \
#   2   3
#  / \
# 4   5

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BreadthFirstSearch
#Iterative - Deque

#         1
#     2      3
#   4   5 
# 


from collections import deque

class Solution(object):
    
    def treeTraversal(self, root):
        if not root:
            return []
        theMainQueue = deque([root])
        theResultsList = []
        while theMainQueue:
            nextLevelQueue = deque()
            currentLevelvals = []
            for eachItem in range(len(theMainQueue)):
                node = theMainQueue.popleft()
                currentLevelvals.append(node.val)
                if node.left:
                    nextLevelQueue.append(node.left)
                if node.right:
                    nextLevelQueue.append(node.right) 
            theResultsList.append(currentLevelvals)
            theMainQueue = nextLevelQueue
        return theResultsList

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        return self.treeTraversal(root)