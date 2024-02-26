import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        print()

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    new_contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(new_contact)
    print(f"\nContact {name} added successfully.\n")

def search_contact(contacts, query):
    matching_contacts = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return matching_contacts

def update_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"\nUpdating contact: {contact['name']}")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email address: ")
            contact['address'] = input("Enter new address: ")
            print(f"\nContact {contact['name']} updated successfully.\n")
            return
    print(f"\nContact {name} not found.\n")

def delete_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"\nContact {name} deleted successfully.\n")
            return
    print(f"\nContact {name} not found.\n")

def main():
    contacts = load_contacts()

    while True:
        print("\n1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            matching_contacts = search_contact(contacts, query)
            display_contacts(matching_contacts)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            update_contact(contacts, name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting contact book. Your contacts have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print("Welcome to the Contact Book!")
    main()
