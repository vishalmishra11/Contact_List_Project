from database_connection import DatabaseConnection

class Contact:

    def __init__(self, name, number, email = None) -> None:
        self.name = name
        self.number = number
        self.email = email

    def __repr__(self) -> str:
        return f"User's name is {self.name}, contact number is {self.number} & email is {self.email}. "
    


class ContactList:
    def __init__(self) -> None:
        self.contacts = []
        self.length = 0

    def takeUserDetails(self): 
        name = input("Enter your name here: ")
        number = input("Enter your number here: ")
        email = input("Enter you email id here: ")
        contact = Contact(name, number, email)
        return contact

    def add_contacts(self): # this is to add contacts to in memory database
        contact = self.takeUserDetails()
        self.contacts.append(contact)
        print(self.contacts)
        self.length += 1


    def create_contact_table(self): # creating contact table first in the database
        
        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            
            cursor.execute('CREATE TABLE IF NOT EXISTS ContactList(name text, number integer, email text)')

    def add_contact_to_the_table(self):

        name = input("Enter your name here: ")
        number = input("Enter your number here: ")
        email = input("Enter your email id here: ")

        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO ContactList VALUES(?, ?, ?)',(name, number, email))
        
        self.length += 1


    def get_all_contacts_from_database(self):

        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM ContactList')
            contacts = cursor.fetchall() # returns tuple as [(name, number, email), (name, number, email)]

            contact = [{'name': row[0], 'number': row[1], 'email': row[2]} for row in contacts]  # converted into dictionaries

            return contact
        
    
    def search_contacts_in_database(self, name):

        with DatabaseConnection('data.db') as connection:

            cursor = connection.cursor()
            cursor.execute('SELECT * FROM ContactList WHERE name = ?', (name,))
            row = cursor.fetchone()
        print(row)

    
    def edit_contacts_in_database(self, name):
        
        new_name = input("Enter the new name you want to update: ")
        new_number = input("Enter the new number here: ")
        new_mail = input("Enter the new mail id here: ")

        with DatabaseConnection('data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE ContactList SET name=?, number=?, email=? WHERE name = ?', (new_name, new_number, new_mail, name))



    def remove_contacts(self, name): # in memory operations
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def search_contact(self, name): # in memory operations
        return next((contact for contact in self.contacts if contact.name == name), None)
    
    def print_number_of_items(self):
        print(self.length)
    
contactList = ContactList()
# contactList.create_contact_table()
# contactList.add_contact_to_the_table()
# print(contactList.get_all_contacts())
contactList.search_contacts_in_database("Vishal Mishra")
#contactList.edit_contacts_in_database("Vishal Kumar Mishra")



