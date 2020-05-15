def song_decoder(song):
    song = song.replace("WUB", " ")

    for i in reversed(range(1, 667)):
        song = song.replace(" " * i, " ")

    if song[0] == " ":
        song = song[1:]
    if song[-1] == " ":
        song = song[:-1]

    return song


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(song_decoder("AWUBBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
