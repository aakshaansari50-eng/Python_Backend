def display_friends(friends):
    for i, j in friends.items():
        print(i + ":", j , "K followers")


friends = {
    "aksha": 8.3,
    "yushra": 7.1,
    "vidhya": 7.7
}

display_friends(friends)