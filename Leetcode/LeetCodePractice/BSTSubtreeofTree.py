# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#if node matches subNode, recurs for left and right in validatorFunction
#if node does not match, recurs for left and right in isSubTree3
#if MainNode is None, return False
#if SubNode is None, return True 


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return False
        if subRoot is None:
            return True
        if self.isMatchValidator(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isMatchValidator(self, node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.isMatchValidator(node1.left,node2.left) and self.isMatchValidator(node1.right,node2.right)
        