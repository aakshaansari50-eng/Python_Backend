from task4 import add_song, remove_song, display_playlist

playlist = []

add_song("Kesariya", playlist)
add_song("Tum hi ho", playlist)
add_song("Girl I need you", playlist)
add_song("Tum se hi", playlist)

remove_song("Ye tune kya kiya", playlist)

display_playlist(playlist)