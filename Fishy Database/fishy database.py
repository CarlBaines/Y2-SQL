import sqlite3 #import

connection = sqlite3.connect('aquarium.db') #connects to a database file.

cursor = connection.cursor() #returns a cursor object which allows SQL statements to be sent to the SQLlite database.


#Menu.
print('-----------------------Welcome to the fishy database-----------------------')

option = int(input('Please enter an option: \n\n 1. Create a table \n 2. Add a fish \n 3. Get all fishes from database  \n 4. Search by name of fish \n 5. Search by fish species \n 6. Search by the tank number of the fish \n 7. Quit '))




if option == 1:
    cursor.execute('CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER);') #line of code that creates the table in the database and assigns the data type of each object.
    print('Table created') #creates table



elif option == 2:
    fishName = input('Please enter the name of the fish ')
    fishSpecies = input('Please enter the species of the fish ')
    tankNumber = int(input('Please enter the tank number for the fish '))

    cursor.execute('INSERT INTO fish (name, species, tank_number)  VALUES (?, ?, ?)', (fishName, fishSpecies, tankNumber)) #create fish.   




elif option == 3:
    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall() #retrieves all the rows in the result set and returns them as a list.
    print(rows)




elif option == 4:  #search the database by fish name

    searchbyName = input('Enter a name to search the fish by ')

    rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name =?", (searchbyName,),).fetchall() #fetches all data of the fish from the database that is equal to the target fish name.
    print(rows)
    



elif option == 5: #search the database by the species of the fish.

    searchbySpecies = input('Enter a species to search the fish by ')

    rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE species =?", (searchbySpecies,),).fetchall() #fetches all data from the database that is equal to the target fish species.
    print(rows)

    


elif option == 6: #search the database by the tank number of the fish.

    searchbyTankNum = int(input('Enter a tank number to search the fish by '))

    rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE tank_number =?", (searchbyTankNum,),).fetchall() #fetches all data from the database that is equal to the target tank number.
    print(rows)


   

elif option == 7:
    quit()


else:
    print('')
    option = int(input('Please enter an option: \n 1. Create a table \n 2. Add a fish \n 3. Get all fishes from database  \n 4. Search by name of fish \n 5. Search by fish species \n 6. Search by the tank number of the fish \n 7. Quit '))


cursor.close() #closes the cursor object.
    
connection.commit() #saves modifications made since the last commit.