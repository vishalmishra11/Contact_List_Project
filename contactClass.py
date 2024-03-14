class Contact:

    def __init__(self, name, number, email = None) -> None:
        self.name = name
        self.number = number
        self.email = email

    def __repr__(self) -> str:
        return f"User's name is {self.name}, contact number is {self.number} & email is {self.email}. "
    
