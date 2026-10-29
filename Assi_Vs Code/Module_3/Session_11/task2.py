import pymysql

mydb = pymysql.connect(host="localhost", user="root", password="")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS music_stream")
mycursor.execute("USE music_stream")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS playlists (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    song_count INT
)
""")

sql = "INSERT INTO playlists (name, song_count) VALUES (%s, %s)"

data = [
    ("Chill Vibes", 15),
    ("Party Songs", 20),
    ("Sad Songs", 8)
]

mycursor.executemany(sql, data)
mydb.commit()

print("3 playlists inserted successfully")

mycursor.close()
mydb.close()