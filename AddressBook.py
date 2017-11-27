
def addContact(name, number):
	new_contact = (name, number)
	contacts.append(new_contact)
	return contacts
def saveContact():
    f = open('ContactAdrress.txt', 'a+')
    for i in contacts:
        f.write("\n{}".format((str(i))))
    saved =contacts.pop()
    f.close()
    return saved

contacts = []


request = input('Do you want to check(type c) or add a new contact(type a)?')

if request == 'a':
    new_name= input("Name: ")
    new_number= input("Number: ")
    addContact(new_name, new_number) and saveContact()

elif request == 'c':
    f= open('ContactAdrress.txt', 'r')
    if f.mode == 'r':
        contents = f.read()
        print(contents)

else:
    pass

