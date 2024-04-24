import mysql.connector

class Database:
    def __init__(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user ='root',
            password = ''
        )

        mycursor = mydb.cursor()
        mycursor.execute('USE DATABASE donasi')
        if mycursor:
            print('Database berhasil dibuat')
        else:
            print('Database gagal dibuat')

#



