# Implementation of Stack with limited size.
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size  # Pre-allocate fixed-size list
        self.top = -1  # Index of the top element

    # Check if the stack is full
    def is_full(self):
        return self.top == self.max_size - 1

    # Check if the stack is empty
    def is_empty(self):
        return self.top == -1

    # Push an element onto the stack
    def push(self, value):
        if self.is_full():
            print("Stack is full! Cannot push", value)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Pushed {value} onto the stack.")

    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        else:
            value = self.stack[self.top]
            self.stack[self.top] = None  # Clear the slot (optional)
            self.top -= 1
            print(f"Popped {value} from the stack.")
            return value

    # Peek at the top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        else:
            return self.stack[self.top]

    # Display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack from top to bottom:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# Example Usage
stack = Stack(3)  # Limited size stack

stack.push(100)
stack.push(200)
stack.push(300)
stack.push(400)  # Should print "Stack is full"

stack.display()

print("Top element is:", stack.peek())

stack.pop()
stack.pop()
stack.pop()
stack.pop()  # Should print "Stack is empty"
