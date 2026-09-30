# def palindrome(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
    
# s=input("Enter a String : ")
# if palindrome(s):
#     print("Is Palindrome!!")
# else:
#     print("Not a Palindrome!!")
def palindrome(s):
    if s==s[::-1]:
        print("Is a Palindrome")
    else:
        print("Not a Palindrome")
    return s
    
s=input("Enter a String : ")
palindrome(s)
    