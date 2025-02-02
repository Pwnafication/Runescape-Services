# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# input  --> 0,3,5,6
# n = 2
# output --> 0,3,6

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node3 = ListNode(6)
node2 = ListNode(5, node3)
node1 = ListNode(3, node2)
head1 = ListNode(0, node1)

n = 2

def destroyNode(head, n):
    if not head:
        return None
    if n == 1:
        return head.next
    cur = head
    while n > 1:
        cur = cur.next
        n -= 1
    cur.next = cur.next.next
    return head

print(destroyNode(head1,n).value)