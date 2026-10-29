import re

text = input("Enter Mobile Number : ")

result = re.search(r"\b[0-9]{10}\b", text)

if result:
    print("Mobile Number:", result.group())
else:
    print("Mobile number not found")