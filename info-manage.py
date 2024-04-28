class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"

class InformationManagementExpertSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)

def main():
    expert_system = InformationManagementExpertSystem()

    while True:
        print("\nInformation Management Expert System")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            expert_system.add_contact(name, phone)
        elif choice == '2':
            expert_system.show_contacts()
        elif choice == '3':
            print("Exiting Information Management Expert System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
