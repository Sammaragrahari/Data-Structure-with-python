# # Implementation of Stack without limited size
class Stack:
    def __init__(self):
        self.s1 = []  # Initialize stack list
        
    def display(self):
        for i in range(len(self.s1) - 1, -1, -1):
            print(self.s1[i])
    
    def push(self, val):
        self.s1.append(val)
        
    def peek_ele(self):
        if self.s1:
            print(self.s1[-1])
        else:
            print("Stack is empty")
        
    def pop_ele(self):
        if self.s1:
            return self.s1.pop()
        else:
            print("Stack is empty")

st = Stack()

st.push('A')
st.push('10')
st.display()
print()
st.push(20)
st.display()



    
            
            