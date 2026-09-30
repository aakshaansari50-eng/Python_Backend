def format_follower_count(n):
    if n >= 1000000:
        return str(n / 1000000) + "M"
    elif n >= 1000:
        return str(n / 1000) + "K"
    else:
        return str(n)


followers = int(input("Enter follower count: "))

print("Followers:", format_follower_count(followers))