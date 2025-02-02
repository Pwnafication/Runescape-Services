# 297. Serialize and Deserialize Binary Tree
# Hard
# Topics
# Companies
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if root is None:
            return "X#"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "#" + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def iteratorFunction(iterativeObject):
            val = next(iterativeObject)
            if val == "X":
                return None
            node = int(val)  # Convert value to integer
            left = iteratorFunction(iterativeObject)
            right = iteratorFunction(iterativeObject)
            return TreeNode(node, left, right)

        iterativeObject = iter(data.split("#"))
        return iteratorFunction(iterativeObject)


# Example Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Test Codec
codec = Codec()
serialized_tree = codec.serialize(root)
print("Serialized:", serialized_tree)  # Expected: "1#2#X#X#3#4#X#X#5#X#X#"

deserialized_tree = codec.deserialize(serialized_tree)
print("Tree Root After Deserialization:", deserialized_tree.val)  # Expected: 1


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))