class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Creating the linked list: 3 -> 2 -> 0 -> -4, and forming a cycle at pos = 1
node3 = ListNode(-4)
node2 = ListNode(0, node3)
node1 = ListNode(2, node2)
head = ListNode(3, node1)

# Forming a cycle (node3 points to node1, at position 1)
node3.next = node1

def findCycle(head: ListNode):
    p1 = head
    p2 = head

    while p2 and p2.next:
        p1 = p1.next  # Slow pointer moves one step
        p2 = p2.next.next  # Fast pointer moves two steps
        
        # If the pointers meet, there is a cycle
        if p1 == p2:
            return "Cycle detected"
    
    return "No cycle"

# Testing the function
print(findCycle(head))
