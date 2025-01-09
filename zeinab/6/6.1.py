class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        return self.stack

    def empty(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def get_size(self):
        return len(self.stack)

    def reverse(self):
        self.stack.reverse()

# Example Usage
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.peek())  
stack.reverse()
print(stack.peek())  
print(stack.is_empty())
print(stack.is_full())
print(stack.get_size())