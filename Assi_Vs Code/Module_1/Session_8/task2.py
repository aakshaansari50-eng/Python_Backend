def artist(song_title):
    dash=song_title.index('-')
    return song_title[dash+2:]

print(artist("Ye Dil Hai Mushkil - Arijit Singh"))