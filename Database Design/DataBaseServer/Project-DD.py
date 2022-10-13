import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mk12291maksim",
    database = "projectfordd2020"
)
mycursor = mydb.cursor()
#mycursor.execute("Create database ProjectForDD2020")
#print("You have created a database called projectfordd2020")
#mycursor.execute("Create table steam_account(steamId int PRIMARY KEY, name varchar(200) NOT NULL, DOB varchar(20), username varchar(200) NOT NULL, address varchar(200))")
#print("You have created a table for the database called steam_account")


print("Welcome to the Steam database management program.")
print("")
while True:
    try:
        
        print("Please choose one of the following options")
        print("1: Enter the data of a user to the database. \n2: Show all of the existing database.")
        print("3: Update information of a user. \n4: Delete a user from the database.")
        print("5: Quit the program.")
        choice = int(input("==>"))
        
        if choice == 1:
            print("1: Add one user. \n2: Add many users \n3: Back to main menu.")
            choice = int(input("==>"))
            if choice == 1:
                id = int(input("Please enter the Id of the user: "))
                name = input("Please enter the full name of the user: ")
                DOB = input("Please enter the date of birth of the user: ")
                username = input("Please enter the username of the user: ")
                address = input("Please enter the address of the user: ")
            
                sqlform = "Insert into steam_account(steamId, name, DOB, username, address) values(%s,%s,%s,%s,%s)"
                steam_account = (id, name, DOB, username, address)
                mycursor.execute(sqlform, steam_account)
                mydb.commit()
                print(mycursor.rowcount, "was inserted")
            
            elif choice == 2:
                while True:
                    id = int(input("Please enter the Id of the user: "))
                    name = input("Please enter the full name of the user: ")
                    DOB = input("Please enter the date of birth of the user: ")
                    username = input("Please enter the username of the user: ")
                    address = input("Please enter the address of the user: ")

                    sqlform = "Insert into steam_account(steamId, name, DOB, username, address) values(%s,%s,%s,%s,%s)"
                    steam_account = (id, name, DOB, username, address)
                    mycursor.execute(sqlform, steam_account)
                    mydb.commit()
                    print(mycursor.rowcount, "was inserted")
                    choice = input("Do you want to continue adding steam users? (y/n)")
                    if choice == 'n':
                        break
            
            elif choice == 3:
                continue
            else:
                print("Please enter option 1-3.")
        elif choice == 2:
            mycursor.execute("Select * from steam_account")
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
        elif choice == 3:
            print("Please choose one of the following parameters you want to be changed to a user.")
            print("1. Update by Identification. \n2. Update by name. \n3. Update by DOB. \n4. Update by Username. \n5. Update by Address \n6. Back to main menu.")
            choice = int(input("==>"))
    
            if choice == 1:
                Id = int(input("Please enter the Id of the user you want to update the information for: "))
                newId = int(input("Please enter the updated Id of the user: "))
                
                sql = "UPDATE steam_account SET steamId = %s WHERE steamId = %s"
                steam_account = (newId, Id)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 2:
                Id = int(input("Please enter the Id of the user you want to update the information for: "))
                newName = input("Please enter the updated full name of the user: ")

                sql = "UPDATE steam_account SET name = %s WHERE steamId = %s"
                steam_account = (newName, Id)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 3:
                Id = int(input("Please enter the Id of the user you want to update the information for: "))
                newDOB = input("Please enter the updated date of birth of the user: ")

                sql = "UPDATE steam_account SET DOB = %s WHERE steamId = %s"
                steam_account = (newDOB, Id)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 4:
                Id = int(input("Please enter the Id of the user you want to update the information for: "))
                newUsername = input("Please enter the updated username of the user: ")

                sql = "UPDATE steam_account SET username = %s WHERE steamId = %s"
                steam_account = (newUsername, Id)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 5:
                Id = int(input("Please enter the Id of the user you want to update the information for: "))
                newAddress = input("Please enter the updated address of the user: ")

                sql = "UPDATE steam_account SET address = %s WHERE steamId = %s"
                steam_account = (newAddress, Id)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 6:
                continue
            
            else:
                print("Please enter option 1-6")
        elif choice == 4:
            print("Please choose one of the following parameters you want to be changed to a user.")
            print("1. Delete a user by Identification. \n2. Delete a user by name. \n3. Delete a user by DOB. \n4. Delete a user by Username.")
            print("5. Delete a user by Address \n6. Back to main menu.")
            choice = int(input("==>"))
            if choice == 1:
                id = int(input("Please enter the Id of the user: "))
                sql = "DELETE FROM steam_account WHERE steamId= %s"
                steam_account = (id,)
                
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 2:
                name = input("Please enter the full name of the user: ")
                sql = "DELETE FROM steam_account WHERE name= %s"
                steam_account = (name,)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 3:
                DOB = input("Please enter the date of birth of the user: ")
                sql = "DELETE FROM steam_account WHERE DOB= %s"
                steam_account = (DOB,)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 4:
                username = input("Please enter the username of the user: ")
                sql = "DELETE FROM steam_account WHERE username= %s"
                steam_account = (username,)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 5:
                address = input("Please enter the address of the user: ")
                sql = "DELETE FROM steam_account WHERE address= %s"
                steam_account = (address,)
                mycursor.execute(sql, steam_account)
                mydb.commit()
            elif choice == 6:
                continue
            else:
                print("Please enter option 1-6 only.")
             
            
        elif choice == 5:
            print("")
            print("Thanks for using the Steam database management program.")
            mydb.close()
            break
            
        
        else:
            print("You have not entered a choice or put a number which is not from 1-5!!!")

    except ValueError:
        print("Please make sure you're using the correct format of entering data.")

