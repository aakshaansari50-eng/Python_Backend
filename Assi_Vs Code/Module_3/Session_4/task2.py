class SongAlreadyExistsError(Exception):
    pass

def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError("Song already exists!")
    playlist.append(song_name)
    print("Song added successfully!")

playlist = ["Kesariya", "Tum hi ho"]

try:
    add_song_to_playlist("Kesariya", playlist)
except SongAlreadyExistsError as e:
    print(e)