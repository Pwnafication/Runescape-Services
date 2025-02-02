class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.globiusMaximus = int('-inf')  # Global maximum path sum

    def maxSumIterator(self, node):
        if node is None:
            return 0

        # Recursively calculate max path sums for left and right subtrees
        left = max(self.maxSumIterator(node.left), 0)  # Ignore negative paths
        right = max(self.maxSumIterator(node.right), 0)

        # Calculate current max path sum considering all combinations
        currentMax = max(node.value,                # Node only
                         left + node.value,         # Node + Left
                         right + node.value,        # Node + Right
                         left + right + node.value) # Node + Left + Right

        # Update the global maximum path sum
        self.globiusMaximus = max(self.globiusMaximus, currentMax)

        # Return potential max (single path sum) to propagate up the tree
        potentialMax = max(node.value, left + node.value, right + node.value)
        return potentialMax

    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxSumIterator(root)
        return self.globiusMaximus
