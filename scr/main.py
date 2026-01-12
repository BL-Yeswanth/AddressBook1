from re import search
from models.contact import Contact
from models.address_book_system import AddressBookSystem
from models.search_person import SearchPerson

class AddressBookMain:
    """
    Entry point of Address Book Program
    """

    def __init__(self):
        self.system = AddressBookSystem()

    def start(self):
        print("Welcome to Address Book Program")

        # =========================
        # UC6: Create / Select Address Book
        # =========================
        while True:
            print("\n1. Create Address Book")
            print("2. Select Address Book")

            choice = input("Choose option (1/2): ")

            if choice == "1":
                name = input("Enter Address Book Name: ")
                self.system.create_address_book(name)
                address_book = self.system.get_address_book(name)
                break

            elif choice == "2":
                self.system.display_address_books()
                name = input("Enter Address Book Name: ")
                address_book = self.system.get_address_book(name)

                if not address_book:
                    print("Address Book not found ❌")
                    continue
                break

            else:
                print("Invalid choice ❌")

        # =========================
        # UC5: Add Multiple Contacts
        # =========================
        while True:
            print("\nEnter Contact Details")

            contact = Contact(
                input("First Name: "),
                input("Last Name: "),
                input("Address: "),
                input("City: "),
                input("State: "),
                input("Zip Code: "),
                input("Phone Number: "),
                input("Email: ")
            )

            address_book.add_contact(contact)

            choice = input("\nAdd another contact? (yes/no): ").lower()
            if choice != "yes":
                break

        # Display Contacts
        address_book.display_contacts()

        # UC3: Edit Contact
        name = input("\nEnter First Name to edit contact: ")
        address_book.edit_contact_by_name(name)

        # UC4: Delete Contact
        name = input("\nEnter First Name to delete contact: ")
        address_book.delete_contact_by_name(name)

        # Final Display
        address_book.display_contacts()
        
        # UC8: Search Person by City or State across Address Books
        search = SearchPerson(self.system.address_books)

        # UC9: View Persons by City
        search.menu()
        
        # UC11: Sort Contacts by Name
        choice = input("\nDo you want to sort contacts by name? (yes/no): ")
        if choice.lower() == "yes":
            address_book.sort_contacts_by_name()



if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
