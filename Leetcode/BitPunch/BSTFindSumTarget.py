class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def hasSum(self, root, target_sum, current_sum):
        if root is None:  # Base case: empty node
            return False

        # Update the current sum
        current_sum += root.value

        # Check if we're at a leaf node and the current sum matches the target sum
        if current_sum == target_sum and root.left is None and root.right is None:
            return True

        # Recursively check the left and right subtrees
        return (self.hasSum(root.left, target_sum, current_sum) or
                self.hasSum(root.right, target_sum, current_sum))

    def hasPathSum(self, root, target_sum):
        return self.hasSum(root, target_sum, 0)


# Helper function to create a binary tree for testing
def create_binary_tree():
    # Level 3
    node7 = TreeNode(7)
    node2 = TreeNode(2)
    node1 = TreeNode(1)

    # Level 2
    node11 = TreeNode(11, node7, node2)
    node13 = TreeNode(13)
    node4_right = TreeNode(4, None, node1)

    # Level 1
    node4_left = TreeNode(4, node11)
    node8 = TreeNode(8, node13, node4_right)

    # Root
    root = TreeNode(5, node4_left, node8)

    return root


# Create a binary tree and test
symmetric_tree = create_binary_tree()
solution = Solution()

target_sum = 22
print(f"Has path sum {target_sum}: {solution.hasPathSum(symmetric_tree, target_sum)}")  # Expected: True
