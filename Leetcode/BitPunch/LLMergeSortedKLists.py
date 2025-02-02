class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @staticmethod
    def create_linked_list(values):
        nodes = [Node(value=value) for value in values]
        for each_index in range(len(nodes) - 1):
            nodes[each_index].next = nodes[each_index + 1]
        return nodes[0] if nodes else None

    @staticmethod
    def merge_two_lists(l1, l2):
        cur = Node(0)  # Dummy node to simplify merging
        ans = cur

        while l1 and l2:
            if l1.value > l2.value:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return ans.next

    @staticmethod
    def merge_k_lists(lists):
        if not lists:
            return None

        last = len(lists) - 1

        while last != 0:
            i = 0
            j = last

            while j > i:
                lists[i] = Node.merge_two_lists(lists[i], lists[j])
                i += 1
                j -= 1

            last = j

        return lists[0]


# Example usage
values_1 = [1, 4, 7]
values_2 = [2, 5, 8]
values_3 = [3, 6, 9]
linked_list_1 = Node.create_linked_list(values_1)
linked_list_2 = Node.create_linked_list(values_2)
linked_list_3 = Node.create_linked_list(values_3)

result = Node.merge_k_lists([linked_list_1, linked_list_2, linked_list_3])

# Print the merged linked list
print("Merged Linked List:")
current = result
while current:
    print(f"Node Value: {current.value}")
    current = current.next
