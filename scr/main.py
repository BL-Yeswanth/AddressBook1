from models.contact import Contact
from models.address_book import AddressBook


class AddressBookMain:
    """
    Entry point of Address Book Program
    """

    def __init__(self):
        self.address_book = AddressBook()

    def start(self):
        print("Welcome to Address Book Program")

        # UC2: Add Contact
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

        self.address_book.add_contact(contact)

        # Display
        self.address_book.display_contacts()

        # UC3: Edit Contact
        name = input("\nEnter First Name to edit contact: ")
        self.address_book.edit_contact_by_name(name)

        # UC4: Delete Contact
        name = input("\nEnter First Name to delete contact: ")
        self.address_book.delete_contact_by_name(name)

        # Final Display
        self.address_book.display_contacts()


if __name__ == "__main__":
    app = AddressBookMain()
    app.start()