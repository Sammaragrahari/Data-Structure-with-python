# Find the sum of given number using recursion 
# n =82614
def Sum(n):
    if n == 0:
        return 0
    else:
        return(n%10)+Sum(n//10)
print(Sum(82614))