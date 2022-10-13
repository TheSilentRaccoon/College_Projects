import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim"
)
mycursor = mydb.cursor()

mycursor.execute("Show databases") #to see what databases are existing
mycursor.execute("Create database project") #to create a new database.

for db in mycursor: # for loop to print out every line
    print(db)