import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="", database="music_stream")

mycursor = mydb.cursor()

sql = "UPDATE playlists SET name = %s WHERE name = %s"
data = ("Chill Hits", "Chill Vibes")

mycursor.execute(sql, data)
mydb.commit()

print("Playlist updated successfully")

mycursor.close()
mydb.close()