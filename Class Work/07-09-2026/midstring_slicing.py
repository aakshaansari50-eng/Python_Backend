#reverse string and check palindrome
"""
s=input("Enter Name :" )

if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
"""

s=input("Enter Name :")
if len(s)%2==0:
   print(s)
else:
   mid=len(s)//2
   print(s[mid-1]+s[mid]+s[mid+1])


