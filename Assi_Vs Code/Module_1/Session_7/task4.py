msg=["Hi","Spam","Hello","Spam","How are you?"]

for i in msg:
    if i=="Spam":
        continue

    if i=="How are you?":
        break
    print(i)