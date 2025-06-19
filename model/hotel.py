from model.address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, address: Address, stars: int):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__address = address
        self.__stars = stars

    @property
    def hotel_id(self): return self.__hotel_id
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value): self.__name = value
    @property
    def address(self): return self.__address
    @property
    def stars(self): return self.__stars
    @stars.setter
    def stars(self, value): self.__stars = value

    def __repr__(self):
        return f"<Hotel {self.name}, {self.stars}★>"

    @classmethod
    def from_row(cls, row, address: Address):
        return cls(row[0], row[1], address, row[2])

    def to_dict(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "stars": self.stars,
            "address": self.address.to_dict()
        }
