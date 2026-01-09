
from models.contact import Contact
from models.address_book import AddressBook
class AddressBookMain:
    
    def start(self):
        print("Welcome to Address Book Program")
        address_book = AddressBook()

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
        address_book.display_contacts()



if __name__ == "__main__":
    app = AddressBookMain()
    app.start()
