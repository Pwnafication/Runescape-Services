# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    
    def iteratorFunction(self,p:TreeNode,q:TreeNode):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            pass
        left = self.iteratorFunction(p.left,q.left)
        right = self.iteratorFunction(p.right,q.right)
        return True
        



    def isSameTree(self, p:TreeNode, q:TreeNode):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return self.isSameTree(p,q)
    