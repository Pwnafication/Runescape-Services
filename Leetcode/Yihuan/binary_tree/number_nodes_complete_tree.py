from math import pow, ceil

class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values):
        queue = [self]
        i = 0
        while queue and i < len(values):
            current = queue.pop(0)
            for side in ["left", "right"]:
                if getattr(current, side) is None:
                    if values[i] is not None:
                        setattr(current, side, TreeNode(values[i]))
                    i += 1
                    if i >= len(values):
                        return self
                if getattr(current, side):
                    queue.append(getattr(current, side))
        return self

# Tree generation
tree = TreeNode()
tree.insert([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, None, None, None])

# Solution Functions
def get_tree_height(root):
    height = 0
    while root and root.left:
        height += 1
        root = root.left
    return height

def node_exists(idx_to_find, height, node):
    left, right = 0, int(pow(2, height)) - 1
    count = 0

    while count < height:
        mid_of_node = ceil((left + right) / 2)
        
        if idx_to_find >= mid_of_node:
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right = mid_of_node - 1
        
        count += 1

    return node is not None

def count_nodes(root):
    if not root:
        return 0

    height = get_tree_height(root)
    if height == 0:
        return 1

    upper_count = int(pow(2, height)) - 1
    left, right = 0, upper_count

    while left < right:
        idx_to_find = ceil((left + right) / 2)
        
        if node_exists(idx_to_find, height, root):
            left = idx_to_find
        else:
            right = idx_to_find - 1

    return upper_count + left + 1

# Perform node counting
print(count_nodes(tree))  # Expected output is the count of nodes in the generated tree
