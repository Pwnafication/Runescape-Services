class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def create_linked_list(values):
        # Create nodes from values
        nodes = [Node(value=value) for value in values]
        # Link nodes together
        for each_index in range(len(nodes) - 1):
            nodes[each_index].next = nodes[each_index + 1]
        return nodes[0]  # Return the head of the linked list

    @staticmethod
    def create_cycle(head, pos):
        if pos == -1:
            return
        # Create a cycle by pointing the last node's next to a node at position 'pos'
        current = head
        target_node = None
        index = 0
        while current.next:
            if index == pos:
                target_node = current
            current = current.next
            index += 1
        current.next = target_node  # Create the cycle

    @staticmethod
    def has_cycle(head):
        tortoise = head
        hare = head
        while hare and hare.next:
            tortoise = tortoise.next  # Move tortoise one step
            hare = hare.next.next  # Move hare two steps
            if tortoise == hare:
                return True  # Cycle detected
        return False  # No cycle


# Create a linked list
values_1 = [1, 2, 5, 7, 8]
linked_list_1 = Node.create_linked_list(values_1)

# Create a cycle in the linked list (e.g., last node points to the node at position 2)
Node.create_cycle(linked_list_1, 2)

# Check if the linked list has a cycle
print("Does the linked list have a cycle?")
print(Node.has_cycle(linked_list_1))  # Output: True
