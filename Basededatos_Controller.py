import sqlite3 as sql


def createDB():
    conn=sql.connect("streamers.db")
    conn.commit()
    conn.close

def createTable():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
        name text, 
        followers integer,
        subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertrow(nombre, followers, subs):
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()



def readRows():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamerList):
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO streamers VALUES (?,?,?)"
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

if __name__=="__main__":
    #createDB()
    #createTable()
    #insertrow("Ibai", 7000000, 25000)
    #insertrow("Alex", 800000, 10000)
    #readRows()
    streamers=[
        ("ElX", 1000000, 2500),
        ("Cristinini", 3000000, 5500),
        ("Auero", 8000000, 54565)
    ]
    #insertRows(streamers)
    readOrdered("subs")
