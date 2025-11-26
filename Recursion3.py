# Reverse a string using recursion
def reverse_string(s):
    if s == "" :
        return s
    else:
        return reverse_string(s[1:])+s[0]
text = "HELLO"
reversed_text= reverse_string(text)
print("Original :",text)
print("Reversed :",reversed_text)