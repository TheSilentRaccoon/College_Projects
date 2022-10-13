import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "project"
)
mycursor = mydb.cursor()

sql = "DELETE FROM employee WHERE name='Maksims'" #if you want to remove an element from a table

mycursor.execute(sql)

mydb.commit()