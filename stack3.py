# Implementation of Stack without  limited size.
class Stack:
    def __init__(self):
        self.stack = []  # Dynamic list, no fixed size

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Push an element onto the stack
    def push(self, value):
        self.stack.append(value)
        print(f"Pushed {value} onto the stack.")

    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        else:
            value = self.stack.pop()
            print(f"Popped {value} from the stack.")
            return value

    # Peek at the top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        else:
            return self.stack[-1]

    # Display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack from top to bottom:")
            for item in reversed(self.stack):
                print(item)


# Example Usage
stack = Stack()  # Unlimited size stack

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

print("Top element is:", stack.peek())

stack.pop()
stack.pop()
stack.pop()
stack.pop()  # Should show "Stack is empty"
