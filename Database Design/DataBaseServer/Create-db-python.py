import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "project"
)
mycursor = mydb.cursor()

mycursor.execute("Create table employee(name varchar(200), sal int (20))")# to create a table
mycursor.execute("Show tables") #view the tables

for tb in mycursor:
    print(tb)