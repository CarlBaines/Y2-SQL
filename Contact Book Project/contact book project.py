import sqlite3
import random
from time import sleep

#creates db file.

connection = sqlite3.connect('contactbook.db')

cursor = connection.cursor()



try: 
    cursor.execute('CREATE TABLE contacts (contact_id INTEGER, name TEXT, phoneNum INTEGER, emailAddress TEXT);') #tests these lines of code for errors.
    
    cursor.execute('CREATE TABLE addresses (address_id INTEGER, houseNum INTEGER, streetName TEXT, postcode TEXT);')

except sqlite3.OperationalError: pass #passes unless there is an operational error which usually means that the table has already been created.


sleep(.5)
print('')
print('----------Welcome to the contact book application----------')
print('')

print('----------Contact Database----------')


databaseOption = int(input('Please select a database to access: \n 1. Contact Database \n 2. Address Database      '))

option = int(input('\nPlease enter an option: \n\n 1. Add new contact records to the database \n 2. Search for contacts by name \n 3. Display all contact records in the database \n 4. Delete contact records from the database \n 5. Modify contact records in the database \n 6. Exit.      '))

if databaseOption == 1: #For Contact Database



    if option == 1:
        #generates a random user ID for a contact. It is then outputted.
        print('')
        contactID = random.randint(111111,999999)
        sleep(.5)
        print('Your contact ID is ' + str(contactID))



        #inputs to put in the contact and address databases.
        sleep(1)
        name = input('Please enter a name to add to the contact database ')
        print('')
        phoneNum = str(input('Please enter a phone number to add to the contact database '))
        print('')
        emailAddress = input('Please enter an email address to add to the contact database ')
        print('')



        #length check for phone number input.
        while len(phoneNum) < 11:
            phoneNum = int(input('Please enter a phone number to add to the database '))


        #validate email address input by checking to see if it contains the '@' symbol.
        count = emailAddress.count('@')

        if count != 1:
            emailAddress = input('Please enter an email address to add to the database ')
        

        #writes details to the databases once checks are made.
        cursor.execute("INSERT INTO contacts (contact_id, name, phoneNum, emailAddress) VALUES (?,?,?,?);", (contactID, name, phoneNum, emailAddress)) #inserts user inputs into database.
        connection.commit()

        print('\nDetails were written to the database ')

    



    elif option == 2:
        #search for contacts by name

        searchbyName = input('Please enter a name to search the database with ')

        rows = cursor.execute("SELECT * FROM contacts WHERE name =?", (searchbyName,),).fetchall()
        #fetches all data from the database that is associated with the name entered by the user; then outputs them.
        print('')
        print(rows)




    elif option == 3:
        rows = cursor.execute("SELECT contact_id, name, phoneNum, emailAddress FROM contacts").fetchall() #retrieves all of the data from the database.
        print('')
        print(rows)





    elif option == 4:
        #enter contact detail you would like to delete.
        deleteContact = input('What contact would you like to delete?\nYou can delete a name, phone number or email address ')

        if deleteContact.lower() == 'name':

            deleteName = input('What name would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE name = ?", (deleteName,))
            print('The name ' + str(deleteName) + ' has been deleted from the database')

        if deleteContact.lower() == 'phone number' or deleteContact.lower() == 'phonenumber':

            deletePhoneNum = input('What phone number would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE phoneNum = ?", (deletePhoneNum,))
            print('The phone number ' + str(deletePhoneNum) + ' has been deleted from the database ')

        if deleteContact.lower() == 'email address' or deleteContact.lower() == 'emailaddress':

            deleteEmailAddress = input('What email address would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE emailAddress = ?", (deleteEmailAddress,))
            print('The email address ' + str(deleteEmailAddress) + ' has been deleted from the database ')





    elif option == 5:
        #Modify contact detail - user enters contact detail to change, deletes it from database and then inputs the modified version into it.
        modifyContact = input('What contact would you like to modify?\nYou can modify a name, phone number or email address ')

        if modifyContact.lower() == 'name':
            modifyName = input('What name would you like to modify in the database? ')

            cursor.execute("DELETE FROM contacts WHERE name = ?", (modifyName,))

            newName = input('Enter the name you would like to replace the original name stored in the database ')
            cursor.execute("INSERT INTO contacts (name)", (newName,))

            print('The new name has been added to the database')



        if modifyContact.lower() == 'phone number' or modifyContact.lower() == 'phonenumber':
            modifyPhoneNum = input('What phone number would you like to modify in the database? ')

            cursor.execute("DELETE FROM contacts WHERE phoneNum = ?", (modifyPhoneNum,))

            newPhoneNumber = input('Enter the name you would like to replace the original phone number stored in the database ')
            cursor.execute("INSERT INTO contacts (phoneNum)", (newPhoneNumber,))

            print('The new phone number has been added to the database')


        if modifyContact.lower() == 'email address' or modifyContact.lower() == 'emailaddress':
            modifyEmailAddress = input('What email address would you like to modify in the database? ')

            cursor.execute("DELETE FROM contacts WHERE emailAddress = ?", (modifyEmailAddress,))

            newEmailAddress = input('Enter the name you would like to replace the original email address stored in the database ')
            cursor.execute("INSERT INTO contacts (emailAddress)", (newEmailAddress,))

            print('The new email address has been added to the database')


    else:
        quit()



            

if databaseOption == 2: #For address database
    print('----------Address Database----------')

    option2 = int(input('Please enter an option: \n\n 1. Add new address records to the database \n 2. Search for addresses by street name \n 3. Display all address records in the database \n 4. Delete address records from the database \n 5. Modify address records in the database \n 6. Exit.      '))
    
    if option2 == 1:

        #generates random address ID. This is then outputted.
        addressID = random.randint(111111,999999)
        sleep(.5)
        print('Your address ID is ' + str(addressID))

        #user inputs to be put in the database.
        houseNumber = str(input('Please enter a house number to add to the address database '))
        print('')
        streetName = input('Please enter a street name to add to the address database ')
        print('')
        postcode = input('Please enter a postcode to add to the address database. Enter with no spaces ')

        #length check for postcode.
        if len(postcode) < 7:
            postcode = input('Please enter a postcode to add to the address database. Enter with no spaces ')

        #add user inputs to the database once checks are made.
        cursor.execute("INSERT INTO addresses (address_id, houseNum, streetName, postCode) VALUES (?,?,?,?);", (addressID, houseNumber, streetName, postcode))
        connection.commit()




    
    elif option2 == 2:
        
        searchbyStreetName = input('Please enter a name to search the database with ')

        rows = cursor.execute("SELECT * FROM addresses WHERE streetName =?", (searchbyStreetName,),).fetchall()
        #fetches all data from the database that is associated with the name entered by the user; then outputs them.
        print('')
        print(rows)




    elif option2 == 3:
        rows = cursor.execute("SELECT address_id, houseNum, streetName, postCode FROM addresses").fetchall() #retrieves all of the data from the database.
        print('')
        print(rows)



    elif option2 == 4:
        #enter address detail you would like to delete.
        deleteAddressDetail = input('What contact would you like to delete?\nYou can delete a house number, street name or postcode. ')

        if deleteAddressDetail.lower() == 'house number' or deleteAddressDetail.lower() == 'housenumber':

            deleteHouseNumber = input('What house number would you like to delete from the database? ')

            cursor.execute("DELETE FROM addresses WHERE houseNum = ?", (deleteHouseNumber,))
            print('The house number ' + str(deleteHouseNumber) + ' has been deleted from the database')



        if deleteAddressDetail.lower() == 'street name' or deleteAddressDetail.lower() == 'streetname':

            deleteStreetName = input('What street name would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE streetName = ?", (deleteStreetName,))
            print('The street name ' + str(deleteStreetName) + ' has been deleted from the database ')




        if deleteAddressDetail.lower() == 'postcode':

            deletePostcode = input('What postcode would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE postCode = ?", (deleteAddressDetail,))
            print('The postcode ' + str(deleteAddressDetail) + ' has been deleted from the database ')



    elif option2 == 5:
        #enter address detail you would like to modify - user enters address detail to change, deletes it from database and then inputs the modified version into it.
        modifyAddressDetail = input('What contact would you like to modify \n You can modify a house number, street name or postcode. ')

        if modifyAddressDetail.lower() == 'house number' or modifyAddressDetail.lower() == 'housenumber':

            modifyHouseNumber = input('What house number would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE houseNum = ?", (modifyHouseNumber,))

            newHouseNumber = input('Enter the name you would like to replace the original house number stored in the database with ')
            cursor.execute("INSERT INTO addresses (houseNum)", (newHouseNumber,))

            print('The new house number has been added to the database')



        if modifyContact.lower() == 'street name' or modifyContact.lower() == 'streetname':
            modifyStreetName = input('What street name would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE streetName = ?", (modifyStreetName,))

            newStreetName = input('Enter the name you would like to replace the original street name stored in the database with ')
            cursor.execute("INSERT INTO addresses (streetName)", (newStreetName,))

            print('The new street name has been added to the database')


        if modifyContact.lower() == 'postcode':
            modifyPostcode = input('What postcode would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE postCode = ?", (modifyPostcode,))

            newPostcode = input('Enter the name you would like to replace the original postcode stored in the database with ')
            cursor.execute("INSERT INTO contacts (postCode)", (newPostcode,))

            print('The new postcode has been added to the database')

    elif option2 == 6:
        quit()



       

