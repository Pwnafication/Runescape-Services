class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def create_linked_list(values):
        nodes = [Node(value=value) for value in values]
        for each_index in range(len(nodes) - 1):
            nodes[each_index].next = nodes[each_index + 1]
        return nodes[0]  # Return the head of the linked list

    @staticmethod
    def remove_nth_node(LL_Head, n):
        dummy = Node(0, LL_Head)  # Add a dummy node to handle edge cases
        first = dummy
        second = dummy

        # Move the first pointer `n + 1` steps ahead to create a gap of `n` between first and second
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node
        second.next = second.next.next

        return dummy.next  # Return the updated linked list (skipping dummy node)

# Example usage
values_1 = [1, 2, 5]
linked_list_1 = Node.create_linked_list(values_1)

# Remove the 1st node from the end
result = Node.remove_nth_node(linked_list_1, n=1)

# Print the resulting linked list
print("Resulting Linked List:")
current = result
while current:
    print(f"Node Value: {current.value}")
    current = current.next
