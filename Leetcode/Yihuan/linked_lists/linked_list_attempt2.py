class ListNode:
    def __init__(self, value=0,next=None):
        self.value = value
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head 
        
        ephemeralNode = ListNode(0)
        ephemeralNode.next = head 
        prev_node = ephemeralNode

        for _ in range(left - 1):
            prev = prev.next 