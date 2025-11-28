def reverse_number(n, rev=0):
    # Base condition
    if n == 0:
        return rev
    
    # Extract last digit and build reversed number
    rev = rev * 10 + (n % 10)
    return reverse_number(n // 10, rev)

def is_palindrome(num):
    if num < 0:
        return False  # Negative numbers are not palindromes
    
    reversed_num = reverse_number(num)
    return num == reversed_num

# ---- Test ----
number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is NOT a palindrome")
