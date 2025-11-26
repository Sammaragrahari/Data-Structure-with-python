#Python lists can be used as stacks using append() and pop():

stack = []
# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)  # [10, 20, 30]

# Pop element
print("Popped:", stack.pop())  # 30
print("Stack after pop:", stack)  # [10, 20]

# Peek (top element)
print("Top element:", stack[-1])  # 20

# Check if empty
print("Is stack empty?", len(stack) == 0)  # False
