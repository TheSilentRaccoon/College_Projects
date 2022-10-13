import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "project"
)
mycursor = mydb.cursor()

mycursor.execute("Select * from employee") #you can change from name to sal to get the salary instead of names

myresult = mycursor.fetchone() # get the first name from the list
myresult = mycursor.fetchall() # get all names from the list

for row in myresult:
    print(row)