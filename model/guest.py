from model.address import Address

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address: Address = None):
        self.__guest_id = guest_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address = address

    @property
    def guest_id(self): return self.__guest_id
    @property
    def first_name(self): return self.__first_name
    @property
    def last_name(self): return self.__last_name
    @property
    def email(self): return self.__email
    @property
    def address(self): return self.__address

    def __repr__(self):
        return f"<Guest {self.first_name} {self.last_name}>"

    @classmethod
    def from_row(cls, row, address: Address = None):
        return cls(row[0], row[1], row[2], row[3], address)

    def to_dict(self):
        return {
            "guest_id": self.guest_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "address": self.address.to_dict() if self.address else None
        }
