# print even and odd number upto the given range using recursion

# for even number
# def evennums(n,e):
#     if n <= e:
#         print(n,end=" ")
#         evennums(n+2,e)
        
# e = int(input("Enter the end value :"))
# evennums(2,e)

# for odd number
def oddnums(n,e):
    if n <= e:
        print(n,end=" ")
        oddnums(n+2,e)
        
e = int(input("Enter the end value :"))
oddnums(1,e)