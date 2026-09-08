#Prompt user to make a selection from the menu options
action = int(input("Please select an Option: \n1. Add \n2. Search \n3. Delete \n4. View All \n5. Exit \n").strip())

#Declare the dictionary
contacts = {'name': '', 'phone' : '', 'email': '' }
name = ''

#Handle user selection input using functions
def add_contact():
    name = input("Enter the contact's name: ").strip()
    contacts['name'] = name
    phone_number = int(input("Enter the contact's phone number: ").strip())
    contacts['phone'] = phone_number
    email = input("Enter the contact's email address: ").strip()
    contacts['email'] = email

def contact_name(name):
    search_name = input("Enter the name you would like to search: ").strip().lower()
    print(f"{contacts.get(search_name, 'Name not found!')}")

def view_all():
    for key, value in contacts.items():
        print(key, value)

def delete_contact(name):
    delete_name = input("Enter the name of the contact you would like to delete: ").strip().lower()
    del contacts[delete_contact]

while True:
    if action == 1:
        add_contact()

    elif action == 2:
        contact_name(name)

    elif action == 3:
        delete_contact(name)

    elif action == 4:
        view_all()
        break

    elif action == 5:
        break
