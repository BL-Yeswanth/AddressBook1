class Contact:
    """
    UC1: Represents a single contact in Address Book
    """
    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
