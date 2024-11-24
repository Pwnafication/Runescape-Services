class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        # Step 1: Create a dummy node and move `prev` to just before `left`
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Initialize pointers for reversal
        start = prev.next        # This is the first node to reverse
        newList = None           # This will be the head of the reversed list

        # Step 3: Reverse nodes in the range [left, right]
        current = start
        current_position = left  # Track position explicitly

        while current_position <= right:
            next_node = current.next  # Temporarily store the next node
            current.next = newList    # Reverse current node by pointing to newList
            newList = current         # Move newList head to current node
            current = next_node       # Move to the next node
            current_position += 1     # Increment position counter

        # Step 4: Reattach the reversed sublist
        prev.next = newList        # Connect the node before `left` to the new head of the reversed sublist
        start.next = current       # Connect the original start (now the tail of the reversed sublist) to the node after `right`

        return dummy.next


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print the linked list for visualization
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Example usage
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverseBetween(head, 2, 4)

print("Reversed portion from position M to N:")
print_linked_list(reversed_head)
