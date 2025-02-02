class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    
    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self, value):
        if not self.main_stack:
            return None
        top_value = self.main_stack.pop()
        if top_value == self.min_stack:
            self.min_stack.pop()
        return top_value
    
    def top(self, value):
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
    
##############################################################################

