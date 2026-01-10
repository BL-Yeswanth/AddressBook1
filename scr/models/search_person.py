class SearchPerson:
    """
    UC8:
    Ability to search Person by City or State
    across multiple Address Books
    """

    def __init__(self, address_books):
        # Dictionary: addressBookName -> AddressBook
        self.address_books = address_books

    # =========================
    # UC8: Search by City
    # =========================
    def search_by_city(self, city):
        results = [
            contact
            for book in self.address_books.values()
            for contact in book.contacts
            if contact.city.lower() == city.lower()
        ]

        if not results:
            print("\nNo persons found in this city ❌")
            return

        print(f"\nPersons found in City '{city}':")
        for c in results:
            print(
                f"{c.first_name} {c.last_name}, "
                f"{c.city}, {c.state}, "
                f"Phone: {c.phone_number}"
            )

    # =========================
    # UC8: Search by State
    # =========================
    def search_by_state(self, state):
        results = [
            contact
            for book in self.address_books.values()
            for contact in book.contacts
            if contact.state.lower() == state.lower()
        ]

        if not results:
            print("\nNo persons found in this state ❌")
            return

        print(f"\nPersons found in State '{state}':")
        for c in results:
            print(
                f"{c.first_name} {c.last_name}, "
                f"{c.city}, {c.state}, "
                f"Phone: {c.phone_number}"
            )
