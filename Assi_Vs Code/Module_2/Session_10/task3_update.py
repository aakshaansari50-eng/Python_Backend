from task3 import add_song, remove_song

playlist = []

add_song("Kesariya", playlist)
add_song("Tum hi ho", playlist)
add_song("Girl I need you", playlist)

remove_song("Shape of You", playlist)

print(playlist)