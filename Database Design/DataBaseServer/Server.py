import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim"

)

print(mydb)

if(mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccesful")