songs = {
    "Kesariya": 4,
    "Tum hi ho": 3,
    "Dare e nijhaad": 5
}

def get_song_duration(name):
    try:
        print(songs[name], "minutes")
    except KeyError:
        print("Song not found on Spotify!")

get_song_duration(input("Enter song name: "))