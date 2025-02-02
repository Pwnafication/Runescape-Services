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
    def merge_linked_lists(linked_list_1, linked_list_2):
        # Create a dummy node to form the new merged list
        dummy = Node(0)
        current = dummy

        # Merge the lists iteratively
        while linked_list_1 and linked_list_2:
            if linked_list_1.value < linked_list_2.value:
                current.next = linked_list_1
                linked_list_1 = linked_list_1.next
            else:
                current.next = linked_list_2
                linked_list_2 = linked_list_2.next
            current = current.next

        # Append remaining nodes from either list
        if linked_list_1:
            current.next = linked_list_1
        if linked_list_2:
            current.next = linked_list_2

        return dummy.next  # Return the merged list starting at dummy.next


# Create two linked lists
values_1 = [1, 2, 5]
linked_list_1 = Node.create_linked_list(values_1)

values_2 = [2, 3, 6]
linked_list_2 = Node.create_linked_list(values_2)

# Print the first linked list
print("Linked List 1:")
current = linked_list_1
while current:
    print(f"Node Value: {current.value}")
    current = current.next

# Print the second linked list
print("\nLinked List 2:")
current = linked_list_2
while current:
    print(f"Node Value: {current.value}")
    current = current.next

# Merge the two linked lists
merged_list = Node.merge_linked_lists(linked_list_1, linked_list_2)

# Print the merged linked list
print("\nMerged Linked List:")
current = merged_list
while current:
    print(f"Node Value: {current.value}")
    current = current.next
