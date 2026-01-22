def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, phone, email = line.strip().split(',')
                contacts.append({'Name': name, 'Phone': phone, 'Email': email})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['Name']},{contact['Phone']},{contact['Email']}\n")

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    contacts.append({'Name': name, 'Phone': phone, 'Email': email})
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
        print()

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contact['Phone'] = input("Enter new Phone: ")
            contact['Email'] = input("Enter new Email: ")
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == name.lower():
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
