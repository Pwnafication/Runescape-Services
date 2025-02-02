class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Creating the linked list: 0 -> 1 -> 2 -> 3
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = ListNode(0, node1)

##############################################################

class Solution:
    @staticmethod
    def reverseLinkedList(head):
        previous = None
        current = head
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = previous   # Reverse the current node's pointer
            previous = current        # Move the previous pointer one step forward
            current = next_node       # Move to the next node in the list
        return previous  # New head of the reversed list

current = head
while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next

print()

# Reversing the linked list
reversed_head = Solution.reverseLinkedList(head)

# Printing the reversed linked list
current = reversed_head
while current:
    print(current.value, end=" -> " if current.next else "")
    current = current.next
# Output: 3 -> 2 -> 1 -> 0
