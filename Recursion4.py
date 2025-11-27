# Print the natural number from reverse order 10 to 1 using recursion
def natural_nums(n):
    if n== 1:
        print(" All natural number display")
    else:
        print(n,"th natural number is display")
        natural_nums(n-1)
natural_nums(10)