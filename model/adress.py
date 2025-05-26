from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.person import Person

class Address:
    def __init__(self, address_id: int, street: str, postal_code: str, city: str, country: str):
        if not address_id or not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street or not isinstance(street, str):
            raise ValueError("street must be a string")
        if not postal_code or not isinstance(postal_code, str):
            raise ValueError("postal_code must be a string")
        if not city or not isinstance(city, str):
            raise ValueError("city must be a string")
        if not country or not isinstance(country, str):
            raise ValueError("country must be a string")
        
        self.__address_id = address_id
        self.__street = street
        self.__postal_code = postal_code
        self.__city = city
        self.__country = country
    
    @property
    def address_id(self): return self.__address_id

    @property
    def street(self): return self.__street
    @street.setter
    def street(self, value): self.__street = value

    @property
    def postal_code(self): return self.__postal_code
    @postal_code.setter
    def postal_code(self, value): self.__postal_code = value

    @property
    def city(self): return self.__city
    @city.setter
    def city(self, value): self.__city = value

    @property
    def country(self): return self.__country
    @country.setter
    def country(self, value): self.__country = value
