contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
        print()

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"\nName: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
            found = True
    if not found:
        print("No contact found.\n")

def update_contact():
    phone = input("Enter phone number of the contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contact['name'] = input("Enter New Name: ")
            contact['phone'] = input("Enter New Phone: ")
            contact['email'] = input("Enter New Email: ")
            contact['address'] = input("Enter New Address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    phone = input("Enter phone number of the contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("------ Contact Manager ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
