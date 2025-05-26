from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address: Address = None):
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = address

    @property
    def hotel_id(self): return self.__hotel_id
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, value): self.__name = value
    @property
    def stars(self): return self.__stars
    @stars.setter
    def stars(self, value): self.__stars = value
    @property
    def address(self): return self.__address
    @address.setter
    def address(self, value): self.__address = value
