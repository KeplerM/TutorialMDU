import sqlite3 as sqlite3

##--Create database
conn=sqlite3.connect('MaterialDataBase.db') #Create database
c=conn.cursor()                             #Create cursor

##--Create Table

c.execute(
    """CREATE TABLE material (
    material_name,
    material_density,
    youngs_modulus_x,
    youngs_modulus_y,
    poisson_ratio_xy,
    poisson_ratio_yz,
    shear_modulus_xy,
    ply_th
    )"""
)

conn.commit()   #Commit changes
conn.close()    #Close connection