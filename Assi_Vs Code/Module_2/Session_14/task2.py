def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    playlists[user][playlist_name].append(song_title)

playlists = {}

add_song_to_playlist(playlists, "raj", "Favourites", "Kesariya", "Arijit Singh")
add_song_to_playlist(playlists, "raj", "Favourites", "Chaleya", "Arijit Singh")

print(playlists)