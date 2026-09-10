#Declare and inittialize the contact book dictionary
contacts = []

# name = ''

# #Implement an add_contact() function that appends a new dictionary to the list
def add_contact():
    name = input("Add the name of the contact: ").strip().lower()
    phone = int(input("Add the contact's phone number: ").strip())
    email = input("Add the contact's email address: ").strip().lower()
    new_contact = { 'name': name, 'phone': phone, 'email': email}

    contacts.append(new_contact)

# #Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)
# def search_contact(name):
#     search_name = input("Enter the name of the contacts you wouldlike to search: ").strip().lower()
#     for searched_contact in contacts:
#         if contacts["name"] == search_name:
#             return searched_contact
#         print(search_contact(search_name))

# #Implement a delete_contact(name) function that removes a contact by name
# def delete_contact(name):
#     delete_name = input("Enter the name of the contact you would like to delete: ").strip().lower()

#Implement a view_all() function that displays all contacts in a formatted layout
def view_all():
    for contact_list in contacts:
        for key, value in contact_list.items():
            print(key, value, "")

# # #Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)
while True:
    action = int(input("Please select an option below: \n1. Add \n2. Search \n3. Delete \n4. View All \n5. Exit \n").strip())
    if action == 1:
        add_contact()
    elif action == 2:
        search_contact(name)
    elif action == 3:
        delete_contact(name)
    elif action == 4:
        view_all()
    elif action == 5:
        break
    else:
        print("Invalid option selected, please try again!")