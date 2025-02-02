# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     1
#    / \
#   2   3
#  / \
# 4   5


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    
    def flipTree(self,node):
        if node is None:
            return None
        left_inverted = self.flipTree(node.left)
        right_inverted = self.flipTree(node.right)

        node.left = right_inverted
        node.right = left_inverted

        return node
        

    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.flipTree(root)
        return root
    

