def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("Enter a string: ")
if palindrome(s):    
    print("The string is a palindrome.")            
else:
    print("The string is not a palindrome.")

"""
def mid_string(s):
    if len(s) % 2 == 0:
        return s
    else:
        mid = len(s) // 2
        return s[mid - 1] + s[mid] + s[mid + 1]

input_string = input("Enter a string: ")
result = mid_string(input_string)
print("The middle string is:", result)
"""
