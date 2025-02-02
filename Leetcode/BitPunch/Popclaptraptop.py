class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store all elements
        self.min_stack = []  # Auxiliary stack to keep track of minimum values

    def push(self, value):
        """Push a value onto the stack."""
        self.stack.append(value)
        # Push the value to the min_stack if it's smaller or equal to the current minimum
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """Remove and return the top value from the stack."""
        if not self.stack:
            return None  # Stack is empty
        top_value = self.stack.pop()
        # If the popped value is the current minimum, pop it from the min_stack as well
        if self.min_stack and top_value == self.min_stack[-1]:
            self.min_stack.pop()
        return top_value

    def top(self):
        """Return the top value of the stack without removing it."""
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """Return the minimum value in the stack."""
        return self.min_stack[-1] if self.min_stack else None

    def __str__(self):
        """Custom string representation for the stack."""
        return f"Stack: {self.stack}\nMin Stack: {self.min_stack}"


# Example usage
stack = MinStack()

# Initialize the stack with some values
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)
stack.push(6)

print("Initial Stack State:")
print(stack)

# Perform some operations
stack.pop()  # Removes 6
print("\nAfter Popping Top:")
print(stack)

print("\nTop Element:", stack.top())  # Should print 2
print("Current Minimum:", stack.getMin())  # Should print 2

stack.pop()  # Removes 2
print("\nAfter Popping Top (again):")
print(stack)

print("Current Minimum:", stack.getMin())  # Should print 3
