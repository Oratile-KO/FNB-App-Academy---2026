contacts = [{'name': 'mosa', 'phone': '0892567453'},
            {'name': 'sli', 'phone': '06673633526'},
            {'name': 'kat', 'phone': '0783728653'}]

name = input(f"Enter the name you want to search: ").strip().lower()
found = False

for search in contacts:
    if  search['name'] == name:
        print(f"Found! {search['name'].capitalize()}'s number is {search['phone']}")
        found = True
if not found:
    print(f"Contact not found!")
