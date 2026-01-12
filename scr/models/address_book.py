from models.contact import Contact
import os

class AddressBook:
    """
    UC2 + UC3 + UC4: Manages contacts in Address Book
    """

    def __init__(self):
        # UC5: Support for Multiple Contacts
        self.contacts = []

    # =========================
    # UC7: Duplicate Check Helper
    # =========================
    def _is_duplicate_contact(self, new_contact):
        # Java Stream equivalent:
        # contacts.stream().anyMatch(c -> c.equals(newContact))
        return any(contact == new_contact for contact in self.contacts)

    # UC2: Add Contact
    def add_contact(self, contact):
        # UC7: Prevent Duplicate Entry
        if self._is_duplicate_contact(contact):
            print(
                f"\nDuplicate Entry ❌ : "
                f"{contact.first_name} already exists."
            )
            return

        self.contacts.append(contact)
        print(
            f"\nContact {contact.first_name} {contact.last_name} added successfully."
        )

    # UC2: Display Contacts
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

    # UC3: Edit Contact
    def edit_contact_by_name(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                print(
                    f"\nEditing contact: "
                    f"{contact.first_name} {contact.last_name}"
                )

                contact.address = input("Enter New Address: ")
                contact.city = input("Enter New City: ")
                contact.state = input("Enter New State: ")
                contact.zip_code = input("Enter New Zip Code: ")
                contact.phone_number = input("Enter New Phone Number: ")
                contact.email = input("Enter New Email: ")

                print("\nContact updated successfully ✅")
                return

        print("\nContact not found ❌")

    # UC4: Delete Contact
    def delete_contact_by_name(self, first_name):
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower():
                self.contacts.remove(contact)
                print(
                    f"\nContact {contact.first_name} "
                    f"{contact.last_name} deleted successfully ✅"
                )
                return

        print("\nContact not found ❌")
        
        # =========================
    # UC11: Sort Contacts by Name
    # =========================
    def sort_contacts_by_name(self):
        if not self.contacts:
            print("\nNo contacts available to sort ❌")
            return

        # Java Streams equivalent: contacts.stream().sorted()
        self.contacts = sorted(
            self.contacts,
            key=lambda c: (c.first_name.lower(), c.last_name.lower())
        )

        print("\nContacts sorted alphabetically by name ✅")
        for contact in self.contacts:
            print(contact)

    # =========================
    # UC12: Sort by City
    # =========================
    def sort_contacts_by_city(self):
        self.contacts.sort(key=lambda c: c.city.lower())
        print("\nContacts sorted by City ✅")
        self.display_contacts()

    # =========================
    # UC12: Sort by State
    # =========================
    def sort_contacts_by_state(self):
        self.contacts.sort(key=lambda c: c.state.lower())
        print("\nContacts sorted by State ✅")
        self.display_contacts()

    # =========================
    # UC12: Sort by Zip
    # =========================
    def sort_contacts_by_zip(self):
        self.contacts.sort(key=lambda c: c.zip_code)
        print("\nContacts sorted by Zip Code ✅")
        self.display_contacts()
        
        
        # =========================
    # UC13: Write Address Book to File
    # =========================
    def write_to_file(self, filename="address_book.txt"):
        if not self.contacts:
            print("\nNo contacts to write ❌")
            return

        with open(filename, "w") as file:
            for contact in self.contacts:
                file.write(
                    f"{contact.first_name},"
                    f"{contact.last_name},"
                    f"{contact.address},"
                    f"{contact.city},"
                    f"{contact.state},"
                    f"{contact.zip_code},"
                    f"{contact.phone_number},"
                    f"{contact.email}\n"
                )

        print(f"\nAddress Book saved to file '{filename}' ✅")

    # =========================
    # UC13: Read Address Book from File
    # =========================
    def read_from_file(self, filename="address_book.txt"):
        try:
            with open(filename, "r") as file:
                print(f"\nReading Address Book from '{filename}':\n")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("\nFile not found ❌")

