class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

u = User("aksha", "aksha@gmail.com")

print(u.username)
print(u.email)