class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        Builds a binary tree from preorder and inorder traversal arrays.
        
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Step 1: Create a hash map for quick lookup of indices in `inorder`
        inorder_index_map = {value: index for index, value in enumerate(inorder)}

        # Step 2: Recursive helper function
        def recurOnMainNode(preorder, inorder):
            # Base case: If the list is empty, return None
            if not preorder or not inorder:
                return None

            # Step 2.1: Root is the first element in preorder
            node_val = preorder[0]
            node = TreeNode(node_val)

            # Step 2.2: Find the index of the root in inorder
            node_index = inorder_index_map[node_val]

            # Step 2.3: Split inorder into left and right subtrees
            left_inorder = inorder[:node_index]
            right_inorder = inorder[node_index + 1:]

            # Step 2.4: Split preorder into left and right subtrees
            left_preorder = preorder[1:len(left_inorder) + 1]
            right_preorder = preorder[len(left_inorder) + 1:]

            # Step 2.5: Recursively build left and right subtrees
            node.left = recurOnMainNode(left_preorder, left_inorder)
            node.right = recurOnMainNode(right_preorder, right_inorder)

            return node

        # Step 3: Call the helper function with the full preorder and inorder
        return recurOnMainNode(preorder, inorder)
