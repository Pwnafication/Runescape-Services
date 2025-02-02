class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Creating the linked lists: 0 -> 3 -> 5 -> 6 and 1 -> 2 -> 4 -> 7
node7 = ListNode(7)
node6 = ListNode(4, node7)
node5 = ListNode(2, node6)
head2 = ListNode(1, node5)

node3 = ListNode(6)
node2 = ListNode(5, node3)
node1 = ListNode(3, node2)
head1 = ListNode(0, node1)

# Creating a third sorted list: 8 -> 9 -> 10
node10 = ListNode(10)
node9 = ListNode(9, node10)
node8 = ListNode(8, node9)
head3 = node8

# List of heads of sorted linked lists
listofLists = [head1, head2, head3]

##############################################################

# Helper function to merge two sorted linked lists
def HelperFunction(head1: ListNode, head2: ListNode) -> ListNode:
    dummyNode = ListNode(-1)  # Placeholder node
    currentNode = dummyNode

    # Merge the two lists
    while head1 and head2:
        if head1.value <= head2.value:
            currentNode.next = head1
            head1 = head1.next
        else:
            currentNode.next = head2
            head2 = head2.next
        currentNode = currentNode.next  # Move the pointer forward

    # Attach the remaining nodes
    if head1:
        currentNode.next = head1
    if head2:
        currentNode.next = head2

    # Return the merged list starting from dummyNode.next
    return dummyNode.next

# Function to merge all sorted lists in listofLists
def MergeSortedLists(listofLists):
    if not listofLists:
        return None
    
    mergedList = listofLists[0]
    for i in range(1,len(listofLists)): 
        mergedList = HelperFunction(mergedList, listofLists)

    return mergedList


# Helper function to print the linked list
def printList(head: ListNode):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Testing the function
merged_head = MergeSortedLists(listofLists)
printList(merged_head)
