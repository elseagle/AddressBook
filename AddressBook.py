"""Day 15: Address Book

Address Book - Create a program that prompts the user for the information in
 most address books (Contact name and phone number) and then stores it in a 
 .txt file! 
 The program shouldalso display the contacts that have been stored in the text
 file
 *list, functions that appends new conatct, function that saves  """
def addContact(name, number):
	new_contact = (name, number)
	contacts.append(new_contact)
	return contacts
contacts = [('Ajayi', '08023097823')]


request = input('Do you want to check(type c) or add a new contact(type a)?')
if request == 'a':
	new_name= input("Name: ")
	new_number= input("Number: ")
	addContact(new_name, new_number)



def saveContact():
    f = open('ContactAdrress.txt', 'w+')
	for i in contacts:
	    f.write(i, "%d\r\n" % (i+1))
    f.close()

if request2 ==  'c':
	saveContact()

