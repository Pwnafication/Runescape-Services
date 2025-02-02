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
    def add_linked_lists(linked_list_1, linked_list_2):
        dummy = Node(value=0)  # Dummy node to serve as the head of the result list
        current = dummy
        carry = 0

        while linked_list_1 or linked_list_2 or carry:
            sum = carry  # Start with the carry from the previous operation

            if linked_list_1:
                sum += linked_list_1.value
                linked_list_1 = linked_list_1.next

            if linked_list_2:
                sum += linked_list_2.value
                linked_list_2 = linked_list_2.next

            # Update carry and create a new node with the sum's last digit
            carry = sum // 10
            current.next = Node(value=sum % 10)

            # Move to the next node in the result list
            current = current.next

        if carry > 0:
            current.next = Node(value=carry)

        return dummy.next  # Return the head of the result list

# Create two linked lists
values_1 = [1, 2, 5]
linked_list_1 = Node.create_linked_list(values_1)

values_2 = [2, 3, 6]
linked_list_2 = Node.create_linked_list(values_2)

# Add the two linked lists
result = Node.add_linked_lists(linked_list_1, linked_list_2)

# Print the resulting linked list
print("Resulting Linked List:")
current = result
while current:
    print(f"Node Value: {current.value}")
    current = current.next
