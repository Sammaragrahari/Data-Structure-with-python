# Check weather string is pallndrome

def ispallindrome(s1):
    if len(s1) == 0:
        return "string is pallindrome"
    elif s1[0] != s1[-1]:
        return "string is not pallindrome"
    else:
        return ispallindrome(s1[1:-1])
    
s1 = "Sammar" 
# s1 = "madam"
print(ispallindrome(s1))