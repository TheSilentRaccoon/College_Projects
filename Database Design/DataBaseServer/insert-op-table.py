import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "project"
)
mycursor = mydb.cursor()

sqlform = "Insert into employee(name,sal) values(%s,%s)"

employees = [("Maksims", 10000), ("Robert", 20000), ("Brian", 40000),]

mycursor.executemany(sqlform, employees)

mydb.commit()