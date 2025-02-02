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
    def oddEvenList(LL_Head):
        odd = LL_Head
        even = odd.next
        evenListHead = odd.next 

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenListHead
        return LL_Head





# Example usage
values_1 = [1, 2, 5, 4]
linked_list_1 = Node.create_linked_list(values_1)

# Remove the 1st node from the end
result = Node.oddEvenList(linked_list_1)

# Print the resulting linked list
print("Resulting Linked List:")
current = result
while current:
    print(f"Node Value: {current.value}")
    current = current.next
