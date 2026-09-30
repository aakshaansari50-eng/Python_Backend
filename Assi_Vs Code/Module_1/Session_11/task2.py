my_playlist = {
    "Kesariya": 4.5,
    "Apna Bana Le": 4.0,
    "Tum Hi Ho": 4.8
}
my_playlist["Chaleya"] = 3.5
my_playlist.update({"Kesariya": 4.8, "Apna Bana Le": 4.2})
my_playlist.update({"Tum Hi Ho": 4.9})

print("Updated playlist:", my_playlist)