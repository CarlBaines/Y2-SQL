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



def contactDatabase():


    sleep(.5)
    print('')

    print('----------Contact Database----------')




    option = input('\nPlease enter an option: \n\n 1. Add new contact records to the database \n 2. Search for contacts by name \n 3. Display all contact records in the database \n 4. Delete contact records from the database \n 5. Modify contact records in the database \n 6. Exit.      ')






    if option == '1':
        #generates a random user ID for a contact. It is then outputted.
        print('')
        contactID = random.randint(111111,999999)
        sleep(.5)
        print('Your contact ID is ' + str(contactID))





        #inputs to put in the contact and address databases.
        sleep(1)
        name = input('Please enter a name to add to the contact database ')
        print('')
        phoneNum = str(input('Please enter a phone number to add to the contact database. 11 numbers must be entered e.g. 07942.....         '))
        print('')



        

        #length check for phone number input.
        while len(phoneNum) != 11:
            print('The phone number inputted is not of the correct length :(')
            phoneNum = int(input('Please enter a phone number to add to the database '))


        emailAddress = input('Please enter an email address to add to the contact database ')
        print('')



        #validate email address input by checking to see if it contains the '@' symbol.
        count = emailAddress.count('@')




        while count != 1:
            print('The email address entered is invalid')
            emailAddress = input('Please enter an email address to add to the database ')
        


        
        #writes details to the databases once checks are made.
        cursor.execute("INSERT INTO contacts (contact_id, name, phoneNum, emailAddress) VALUES (?,?,?,?);", (contactID, name, phoneNum, emailAddress)) #inserts user inputs into database.
        connection.commit()

        print('Details were written to the database ')

        returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

        sleep(.5)
        contactDatabase()





    



    if option == '2':
        #search for contacts by name

        searchbyName = input('Please enter a name to search the database with ')

        rows = cursor.execute("SELECT * FROM contacts WHERE name =?", (searchbyName,),).fetchall()

        if len(rows) == 0:
            print('No search results have been found in the database for the inputted name')
            searchbyName = input('Please re-enter a name to search the database with ')

        else:
            #fetches all data from the database that is associated with the name entered by the user; then outputs them.
            print('')
            print(rows[0])

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            contactDatabase()




    if option == '3':
        rows = cursor.execute("SELECT contact_id, name, phoneNum, emailAddress FROM contacts").fetchall() #retrieves all of the data from the database.
        print('')
        print(rows[0])

        returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

        sleep(.5)
        contactDatabase()




    if option == '4':
        #enter contact detail you would like to delete.
        deleteContact = input('What contact would you like to delete?\nYou can delete a name, phone number or email address ')

        while True:
            if deleteContact.lower() == 'name':
            
                deleteName = input('\nWhat name would you like to delete from the database? ')

                cursor.execute("DELETE FROM contacts WHERE name = ?", (deleteName,)) #sql statement searches for the name that the user inputted in the contacts database.
                print('The name ' + str(deleteName) + ' has been deleted from the database')

                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()




            else:
                print('')
                print('The inputted name cannot be deleted as it has not been found within the database :(')
                break




        while True:

            if deleteContact.lower() == 'phone number' or deleteContact.lower() == 'phonenumber':

                deletePhoneNum = input('\nWhat phone number would you like to delete from the database? ')

                cursor.execute("DELETE FROM contacts WHERE phoneNum = ?", (deletePhoneNum,)) 
                print('The phone number ' + str(deletePhoneNum) + ' has been deleted from the database ')

                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()




            else:
                print('')
                print('The inputted phone number cannot be deleted as it has not been found within the database :(')
                break




        while True:

            if deleteContact.lower() == 'email address' or deleteContact.lower() == 'emailaddress':

                deleteEmailAddress = input('\nWhat email address would you like to delete from the database? ')

                cursor.execute("DELETE FROM contacts WHERE emailAddress = ?", (deleteEmailAddress,))
                print('The email address ' + str(deleteEmailAddress) + ' has been deleted from the database ')

                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()




            else:
                print('')
                print('The inputted email address cannot be deleted as it has not been found within the database :(')
                break





    if option == '5':
        #Modify contact detail - user enters contact detail to change, deletes it from database and then inputs the modified version into it.
        modifyContact = input('What contact would you like to modify?\nYou can modify a name, phone number or email address ')




        while True:
                
            if modifyContact.lower() == 'name':
                modifyName = input('\nWhat name would you like to modify in the database? ')

                cursor.execute("DELETE FROM contacts WHERE name = ?", (modifyName,))    #sql statements search for the inputted name within the contacts database, deletes it and inserts the modified version into the database.

                newName = input('Enter the name you would like to replace the original name stored in the database ')
                cursor.execute("INSERT INTO contacts (name)", (newName,))

                print('The new name has been added to the database')
                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()




            else:
                print('')
                print('The name in the database could not be modified as it cannot be found')
                break




        while True:

            if modifyContact.lower() == 'phone number' or modifyContact.lower() == 'phonenumber':
                modifyPhoneNum = input('\nWhat phone number would you like to modify in the database? ')

                cursor.execute("DELETE FROM contacts WHERE phoneNum = ?", (modifyPhoneNum,))

                newPhoneNumber = input('Enter the name you would like to replace the original phone number stored in the database ')
                cursor.execute("INSERT INTO contacts (phoneNum)", (newPhoneNumber,))

                print('The new phone number has been added to the database')
                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()




            else:
                print('')
                print('The phone number in the database could not be modified as it cannot be found')
                break




        while True:

            if modifyContact.lower() == 'email address' or modifyContact.lower() == 'emailaddress':
                modifyEmailAddress = input('\nWhat email address would you like to modify in the database? ')

                cursor.execute("DELETE FROM contacts WHERE emailAddress = ?", (modifyEmailAddress,))

                newEmailAddress = input('Enter the name you would like to replace the original email address stored in the database ')
                cursor.execute("INSERT INTO contacts (emailAddress)", (newEmailAddress,))

                print('The new email address has been added to the database')
                returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

                sleep(.5)
                contactDatabase()



            else:
                print('')
                print('The email address in the database could not be modified as it cannot be found')
                break




    else:
        quit()







def addressDatabase():


    print('----------Address Database----------')

    option2 = input('Please enter an option: \n\n 1. Add new address records to the database \n 2. Search for addresses by street name \n 3. Display all address records in the database \n 4. Delete address records from the database \n 5. Modify address records in the database \n 6. Exit.      ')
    


    if option2 == '1':

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




        #add user inputs to the database once checks are made, using the SQL statement.
        cursor.execute("INSERT INTO addresses (address_id, houseNum, streetName, postCode) VALUES (?,?,?,?);", (addressID, houseNumber, streetName, postcode))
        connection.commit()




    

    elif option2 == '2':
        


        searchbyStreetName = input('Please enter a name to search the database with ')



        rows = cursor.execute("SELECT * FROM addresses WHERE streetName =?", (searchbyStreetName,),).fetchall()
        #fetches all data from the database that is associated with the name entered by the user; then outputs them. This is done by using a select wildcard sql statement.
        print('')
        print(rows[0])

        returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

        sleep(.5)
        addressDatabase()





    elif option2 == '3':
        rows = cursor.execute("SELECT address_id, houseNum, streetName, postCode FROM addresses").fetchall() #retrieves all of the data from the database.
        print('')
        print(rows[0])

        returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

        sleep(.5)
        addressDatabase()






    elif option2 == '4':
        #enter address detail you would like to delete.
        deleteAddressDetail = input('What contact would you like to delete?\nYou can delete a house number, street name or postcode. ')





        if deleteAddressDetail.lower() == 'house number' or deleteAddressDetail.lower() == 'housenumber':

            deleteHouseNumber = input('\nWhat house number would you like to delete from the database? ')

            cursor.execute("DELETE FROM addresses WHERE houseNum = ?", (deleteHouseNumber,))
            print('')
            print('The house number ' + str(deleteHouseNumber) + ' has been deleted from the database')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()






        else:
            print('')
            print('The selected house number cannot be deleted as it was not found in the database')






        if deleteAddressDetail.lower() == 'street name' or deleteAddressDetail.lower() == 'streetname':

            deleteStreetName = input('\nWhat street name would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE streetName = ?", (deleteStreetName,))
            print('')
            print('The street name ' + str(deleteStreetName) + ' has been deleted from the database ')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()



        else:
            print('')
            print('The selected street name cannot be deleted as it was not found in the database')







        if deleteAddressDetail.lower() == 'postcode':

            deletePostcode = input('\nWhat postcode would you like to delete from the database? ')

            cursor.execute("DELETE FROM contacts WHERE postCode = ?", (deleteAddressDetail,))
            print('')
            print('The postcode ' + str(deletePostcode) + ' has been deleted from the database ')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()





        else:   
            print('')
            print('The selected postcode cannot be deleted as it was not found in the database')






    if option2 == '5':
        #enter address detail you would like to modify - user enters address detail to change, deletes it from database and then inputs the modified version into it.
        modifyAddressDetail = input('What contact would you like to modify \n You can modify a house number, street name or postcode. ')






        if modifyAddressDetail.lower() == 'house number' or modifyAddressDetail.lower() == 'housenumber':

            modifyHouseNumber = input('\nWhat house number would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE houseNum = ?", (modifyHouseNumber,))

            newHouseNumber = input('Enter the name you would like to replace the original house number stored in the database with ')
            cursor.execute("INSERT INTO addresses (houseNum)", (newHouseNumber,))

            print('The new house number has been added to the database')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()





        else:
            print('')
            print('The inputted house number could not be modified because it was not found in the database')







        if modifyAddressDetail.lower() == 'street name' or modifyAddressDetail.lower() == 'streetname':
            modifyStreetName = input('\nWhat street name would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE streetName = ?", (modifyStreetName,))

            newStreetName = input('Enter the name you would like to replace the original street name stored in the database with ')
            cursor.execute("INSERT INTO addresses (streetName)", (newStreetName,))

            print('The new street name has been added to the database')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()





        else:
            print('')
            print('The inputted house number could not be modified because it was not found in the database')






        if modifyAddressDetail.lower() == 'postcode':
            modifyPostcode = input('\nWhat postcode would you like to modify in the database? ')

            cursor.execute("DELETE FROM addresses WHERE postCode = ?", (modifyPostcode,))

            newPostcode = input('Enter the name you would like to replace the original postcode stored in the database with ')
            cursor.execute("INSERT INTO contacts (postCode)", (newPostcode,))

            print('The new postcode has been added to the database')

            returnToMenu = input('\n--PRESS ENTER TO RETURN TO THE CONTACT BOOK MENU-- ')

            sleep(.5)
            addressDatabase()





        else:
            print('')
            print('The inputted postcode could not be modified because it was not found in the database')





    if option2 == 6:
        quit()






#A function for the different databases is called depending on the option of the user.
print('')
databaseOption = input('Please select a database to access: \n 1. Contact Database \n 2. Address Database      ')


if databaseOption == '1':
    contactDatabase()



elif databaseOption == '2':
    addressDatabase()




       

