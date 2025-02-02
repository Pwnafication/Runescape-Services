class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []  # Stack to handle enqueue operations
        self.stack_out = []  # Stack to handle dequeue and peek operations

    def enqueue(self, value):
        # Push the new element onto the input stack
        self.stack_in.append(value)

    def dequeue(self):
        # Check if stack_out is empty, transfer elements if necessary
        if not self.stack_out:
            while self.stack_in:
                # Move all elements from stack_in to stack_out
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out, which is the front of the queue
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("dequeue from an empty queue")

    def peek(self):
        # Ensure elements are in stack_out for the front element
        if not self.stack_out:
            while self.stack_in:
                # Move elements to stack_out if it's empty
                self.stack_out.append(self.stack_in.pop())
        # The last element in stack_out is the front of the queue
        if self.stack_out:
            return self.stack_out[-1]
        else:
            raise IndexError("peek from an empty queue")

    def empty(self):
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out
