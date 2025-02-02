class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    
    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            return None
        top_value = self.main_stack.pop()
        if self.min_stack and top_value == self.min_stack[-1]:
            self.min_stack.pop()
        return top_value
    
    def top(self):
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None


##############################################################################

# Parenthesis Matching Logic
parenthesis = {
    "(": ")",
    "[": "]",
    "{": "}",
}
input_string = "(hello())"

# Stack for parenthesis matching
stack = MinStack()

def is_balanced(input_string):
    for char in input_string:
        if char in parenthesis.keys():  # Open parenthesis
            stack.push(char)
        elif char in parenthesis.values():  # Close parenthesis
            if not stack.main_stack or parenthesis[stack.pop()] != char:
                return False

    # If stack is empty, all parentheses were matched
    return not stack.main_stack

# Test the function
print("Is the input string balanced?:", is_balanced(input_string))
