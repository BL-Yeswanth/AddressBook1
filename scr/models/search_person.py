class SearchPerson:
    """
    UC8 + UC9 + UC10:
    Search, View and Count Persons across multiple Address Books
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

    # =========================
    # UC9: View Persons by City
    # =========================
    def view_persons_by_city(self):
        city_dict = {}

        for book in self.address_books.values():
            for contact in book.contacts:
                city = contact.city
                city_dict.setdefault(city, []).append(contact)

        if not city_dict:
            print("\nNo contacts available ❌")
            return

        print("\nPersons grouped by City:")
        for city, persons in city_dict.items():
            print(f"\nCity: {city}")
            for p in persons:
                print(f"  - {p.first_name} {p.last_name}")

    # =========================
    # UC9: View Persons by State
    # =========================
    def view_persons_by_state(self):
        state_dict = {}

        for book in self.address_books.values():
            for contact in book.contacts:
                state = contact.state
                state_dict.setdefault(state, []).append(contact)

        if not state_dict:
            print("\nNo contacts available ❌")
            return

        print("\nPersons grouped by State:")
        for state, persons in state_dict.items():
            print(f"\nState: {state}")
            for p in persons:
                print(f"  - {p.first_name} {p.last_name}")

    # =========================
    # UC10: Count by City
    # =========================
    def count_by_city(self):
        city_count = {}

        for book in self.address_books.values():
            for contact in book.contacts:
                city_count[contact.city] = city_count.get(contact.city, 0) + 1

        if not city_count:
            print("\nNo contacts available ❌")
            return

        print("\nContact Count by City:")
        for city, count in city_count.items():
            print(f"{city} : {count}")

    # =========================
    # UC10: Count by State
    # =========================
    def count_by_state(self):
        state_count = {}

        for book in self.address_books.values():
            for contact in book.contacts:
                state_count[contact.state] = state_count.get(contact.state, 0) + 1

        if not state_count:
            print("\nNo contacts available ❌")
            return

        print("\nContact Count by State:")
        for state, count in state_count.items():
            print(f"{state} : {count}")

    # =========================
    # MENU CONTROLLER
    # =========================
    def menu(self):
        while True:
            print("\nSearch & View Menu")
            print("1. Search Person by City")
            print("2. Search Person by State")
            print("3. View Persons by City")
            print("4. View Persons by State")
            print("5. Count Persons by City")
            print("6. Count Persons by State")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                city = input("Enter City Name: ")
                self.search_by_city(city)
            elif choice == "2":
                state = input("Enter State Name: ")
                self.search_by_state(state)
            elif choice == "3":
                self.view_persons_by_city()
            elif choice == "4":
                self.view_persons_by_state()
            elif choice == "5":
                self.count_by_city()
            elif choice == "6":
                self.count_by_state()
            elif choice == "7":
                break
            else:
                print("Invalid choice ❌ Please try again.")
