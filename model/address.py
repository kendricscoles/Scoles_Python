class Address:
    def __init__(self, address_id: int, street: str, city: str, postal_code: str, country: str = "Switzerland"):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__postal_code = postal_code
        self.__country = country

    @property
    def address_id(self): return self.__address_id
    @property
    def street(self): return self.__street
    @street.setter
    def street(self, value): self.__street = value
    @property
    def city(self): return self.__city
    @city.setter
    def city(self, value): self.__city = value
    @property
    def postal_code(self): return self.__postal_code
    @postal_code.setter
    def postal_code(self, value): self.__postal_code = value
    @property
    def country(self): return self.__country

    def __repr__(self):
        return f"<Address {self.street}, {self.city}, {self.postal_code}, {self.country}>"

    @classmethod
    def from_row(cls, row):
        return cls(*row)

    def to_dict(self):
        return {
            "address_id": self.address_id,
            "street": self.street,
            "city": self.city,
            "postal_code": self.postal_code,
            "country": self.country
        }
