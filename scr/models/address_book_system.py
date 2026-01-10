from models.address_book import AddressBook


class AddressBookSystem:
    """
    UC6: Manages multiple Address Books
    """

    def __init__(self):
        # Dictionary: AddressBook Name -> AddressBook Object
        self.address_books = {}

    def create_address_book(self, name):
        if name in self.address_books:
            print("\nAddress Book already exists ❌")
        else:
            self.address_books[name] = AddressBook()
            print(f"\nAddress Book '{name}' created successfully ✅")

    def get_address_book(self, name):
        return self.address_books.get(name)

    def display_address_books(self):
        if not self.address_books:
            print("\nNo Address Books available.")
            return

        print("\nAvailable Address Books:")
        for name in self.address_books:
            print(f"- {name}")
