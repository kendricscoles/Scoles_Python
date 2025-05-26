from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType

class Room:
    def __init__(self, room_id: int, room_no: str, price_per_night: float, room_type: RoomType, hotel: Hotel):
        if not room_id or not isinstance(room_id, int):
            raise ValueError("room_id must be an integer")
        if not room_no or not isinstance(room_no, str):
            raise ValueError("room_no must be a string")
        if not isinstance(price_per_night, (float, int)):
            raise ValueError("price_per_night must be a float")
        
        self.__room_id = room_id
        self.__room_no = room_no
        self.__price_per_night = float(price_per_night)
        self.__room_type = room_type
        self.__hotel = hotel

    @property
    def room_id(self): return self.__room_id

    @property
    def room_no(self): return self.__room_no
    @room_no.setter
    def room_no(self, value): self.__room_no = value

    @property
    def price_per_night(self): return self.__price_per_night
    @price_per_night.setter
    def price_per_night(self, value): self.__price_per_night = float(value)

    @property
    def room_type(self): return self.__room_type
    @room_type.setter
    def room_type(self, value): self.__room_type = value

    @property
    def hotel(self): return self.__hotel
    @hotel.setter
    def hotel(self, value): self.__hotel = value
