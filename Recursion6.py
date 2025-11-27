# Convert given decimal to binary without using loop
def dec(n):
    if n>1:
        dec(n//2)
    print(n%2,end= "")
dec(15)