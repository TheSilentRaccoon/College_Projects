import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "project"
)
mycursor = mydb.cursor()

sql = "UPDATE employee SET sal=70000 WHERE name='Robert'"

mycursor.execute(sql)

mydb.commit()