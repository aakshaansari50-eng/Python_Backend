import pymysql

def delete_playlist(id):
    mydb = None

    try:
        mydb = pymysql.connect(host="localhost", user="root", password="", database="music_stream")
        mycursor = mydb.cursor()

        mycursor.execute("DELETE FROM playlists WHERE id = %s", (id,))
        mydb.commit()

        if mycursor.rowcount > 0:
            print("Playlist deleted successfully")
        else:
            print("Playlist ID not found")

        mycursor.close()

    except pymysql.MySQLError:
        print("Error occurred")

    finally:
        if mydb:
            mydb.close()

id = int(input("Enter playlist ID: "))
delete_playlist(id)