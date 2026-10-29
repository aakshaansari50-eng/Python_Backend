class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1

post = InstagramPost("My Photo", 10, ["Nice pic"])

post.add_comment("Beautiful!")
print("Caption:", post.caption)
print("Likes:", post.likes)
print("Comments:", post.comments)