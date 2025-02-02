from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def Level_Order_List(node):
    result = []
    queue = deque([node])
    
    while len(queue):    
        Q_Length = len(queue)
        Count = 0
        current_level_list = []

        while Count < Q_Length:
            current_node = queue.popleft()
            current_level_list.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            Count +=1

        Count = len(queue)
        result.append(current_level_list)
    return result

# Creating a binary search tree for the example
#       10
#      /   \
#     5     15
#    / \   /  \
#   3   7 12  18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Perform
result = Level_Order_List(root)
print(result)  
