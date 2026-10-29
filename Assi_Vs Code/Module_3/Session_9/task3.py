import re

def extract_hashtags(text):
    return re.findall(r"#[A-Za-z0-9_]+", text)

text = input("Enter Instagram caption: ")
print(extract_hashtags(text))