contacts = {}  # Dictionary to store contacts

print("📒 Contact Book")

while True:
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added successfully.")

    elif choice == "2":
        name = input("Enter contact name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print(f"{name}'s contact updated.")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if not contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
