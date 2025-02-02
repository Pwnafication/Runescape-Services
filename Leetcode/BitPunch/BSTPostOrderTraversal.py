class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Create a 5-level valid BST
def create_5_level_bst():
    # Level 5
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node21 = TreeNode(21)
    node24 = TreeNode(24)
    node26 = TreeNode(26)
    node29 = TreeNode(29)
    
    # Level 4
    node3 = TreeNode(3, node1, node4)
    node7 = TreeNode(7, node6, node9)
    node23 = TreeNode(23, node21, node24)
    node27 = TreeNode(27, node26, node29)
    
    # Level 3
    node5 = TreeNode(5, node3, node7)
    node25 = TreeNode(25, node23, node27)
    
    # Level 2
    node15 = TreeNode(15, node5, None)
    node30 = TreeNode(30, None, node25)
    
    # Level 1 (Root)
    root = TreeNode(20, node15, node30)
    
    return root


################################################################################################

root = create_5_level_bst()

#pre-order (node,left,right)
#in-order (left, node, right)
#post-order (left,right,node)



def recursiveIterator(node: TreeNode, collective_list: list):
    if not node:
        return
    
    recursiveIterator(node.left, collective_list)
    recursiveIterator(node.right, collective_list)

    collective_list.append(node.value)
    

def postOrderTraversal(root: TreeNode):
    collective_list = []
    node = root
    recursiveIterator(node, collective_list)
    return collective_list

print(postOrderTraversal(root))



#         4
#     2       6
#    1 3     5 7