class ContactList:


    def contact_info(self, first_name, last_name, number, image, call: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.image = image
        self.call = call
        call = False
    

    @property
    def get_number(self):
        return self.get_number
    
    @get_number.setter
    def number(self, number_is):
        if not (isinstance(number_is, int)):
            return f"That is an invalid input. Number must be numerical in format."
        elif (9 < number_is):
            return f"I'm sorry, there are not enough characters in your phone number. The phone number must be at least 9 numbers long."
        elif (10 > number_is):
            return f"I'm sorry, there are too many characters in your phone number. The phone number cannot be longer than 10 numbers long."
        self._number = number_is
        

    def __str__(self):
        return (
            f"""
            Contacts:
            Name: {self.last_name}, {self.first_name}
            Number: {self.number}
            Profile Image: {self.image}
            Recently Called: {self.call}
            """)
        


    #def add_contact({})