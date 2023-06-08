import sqlite3 as sql


def createDB():
    conn=sql.connect("FUMD_Database.db")
    conn.commit()
    conn.close

def createTable():
    conn=sql.connect("FUMD_Database.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE FUMD_Database (
        plies integer, 
        orientation_groups integer,
        m_one integer,
        m_two integer,
        m_three integer,
        m_four integer,
        m_five integer,
        stacking_sequence text
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

def insertRows(RawList):
    conn=sql.connect("FUMD_Database.db")
    cursor=conn.cursor()
    instruccion=f"INSERT INTO FUMD_Database VALUES (?,?,?,?,?,?,?,?)"
    cursor.executemany(instruccion, RawList)
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

def search():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers WHERE subs > 6000 ORDER BY subs DESC"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def updateFields():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"UPDATE streamers SET followers=1200000 WHERE name like 'El%'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()

def deleteRow():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"DELETE FROM streamers WHERE name='Alex'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()

def filtrar():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT * FROM streamers WHERE subs > 6000 AND name='Auero'"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def Lista():
    conn=sql.connect("streamers.db")
    cursor=conn.cursor()
    instruccion=f"SELECT DISTINCT name FROM streamers"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    lista=list(datos)
    print(lista)
   

if __name__=="__main__":
    #createDB()
    #createTable()
    #insertrow("Ibai", 7000000, 25000)
    #insertrow("Alex", 800000, 10000)
    #readRows()
    
    #readOrdered("subs")
    #search()
    #updateFields()
    #deleteRow()
    #filtrar()
    #Lista()
    raw=[
        (7,0,0,0,0,0,0,0),
        (8,0,0,0,0,0,0,0)
        
    ]
    insertRows(raw)
