def num(n,e):
    if n < e:
        print(n,end=" ")
        num(n+1,e)
    print(n,end=" ")

e = int(input("Enter the end value :"))
num(1,e)
    