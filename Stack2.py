# Implementation of Stack with limited size
class Stack:
    def __init__(self,maxsize):
        self.s1 = []
        self.maxsize = maxsize
        
    def Isfull(self):
        if len(self.s1) == self.maxsize:
            return True
        else:
            return False
        
    def IsEmpty(self):
        if len(self.s1) == 0:
            return True
        else:
            return False
        
    def push(self,val):
        if self.Isfull():
            print("Stack is full")
        else:
            self.s1.append(val)
            
    def pop_ele(self):
        if self.IsEmpty():
            print(" No element in Stack ")
        else:
            print(self.s1.pop())
            
    def display(self):
        if self.IsEmpty():
            print(" No element to display")
        else:
            for i in range (len(self.s1)-1,-1,-1):
                print(self.s1[i])
        
    def peek_ele(self):
        if self.IsEmpty():
            print(" No element to peek")
        else:
            print(self.s1[-1])

st = Stack(5)
while True:
    print(".............................Stack Operation..........................")
    print("1.IsFull\n2.IsEmpty\n3.Push\n4.Pop\n5.Display\n6.Peek")
    opt = int(input("Enter your option: "))
    match opt:
        case 1:
            print("Is Stack is full --->",st.Isfull())
        case 2:
            print("Is Stack is empty --->",st.IsEmpty())
        case 3:
            val = input("Enter the value to push()")
            st.push(val)
        case 4:
            st.pop_ele()
        case 5:
            st.display()
        case 6:
            st.peek_ele()
        case _:
            print("Invalid option")
            
        
            
            
        

        
        