# Sum of numbers using recursion
def sum_numbers(n):
    if n == 0: # Base case
        return 0
    else:
        return n + sum_numbers(n-1)  #Recursive case
print(sum_numbers(5)) # output: 15
    