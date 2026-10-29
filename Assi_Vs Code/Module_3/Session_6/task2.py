class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

i = Influencer("aksha", "aksha@gmail.com", 5000)

print(i.username)
print(i.email)
print(i.followers)