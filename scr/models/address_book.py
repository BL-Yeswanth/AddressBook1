from models.contact import Contact


class AddressBook:
    """
    UC2: Manages contacts in Address Book
    """

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(
            f"\nContact {contact.first_name} {contact.last_name} added successfully."
        )

    def display_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
            return

        print("\nAddress Book Contacts:")
        for contact in self.contacts:
            print(
                f"{contact.first_name} {contact.last_name}, "
                f"{contact.city}, {contact.state}, "
                f"Phone: {contact.phone_number}"
            )
