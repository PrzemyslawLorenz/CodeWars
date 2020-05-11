def friend(x):
    myFriends = []
    for name in x:
        if len(name) == 4:
            myFriends.append(name)

    return myFriends


print(friend(["This", "IS", "enough", "TEst", "CaSe"]))
