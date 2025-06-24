contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Added!\n")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts yet.\n")
        return
    print("\nContacts:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    term = input("Search by name or phone: ")
    found_any = False
    for c in contacts:
        if term.lower() in c['name'].lower() or term in c['phone']:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found_any = True
    if not found_any:
        print("No matching contact found.\n")

def update_contact():
    phone = input("Phone number of contact to update: ")
    for c in contacts:
        if c['phone'] == phone:
            c['name'] = input("New name: ")
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            c['address'] = input("New address: ")
            print("Updated!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    phone = input("Phone number of contact to delete: ")
    for c in contacts:
        if c['phone'] == phone:
            contacts.remove(c)
            print("Deleted!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("Contact Manager")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("Choose (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Bye!")
            break
        else:
            print("Try again.\n")

menu()
