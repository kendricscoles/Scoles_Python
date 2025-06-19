from model.room_type import RoomType
from model.hotel import Hotel

class Room:
    def __init__(self, room_id: int, room_number: str, price_per_night: float, hotel: Hotel, room_type: RoomType):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__hotel = hotel
        self.__room_type = room_type

    @property
    def room_id(self): return self.__room_id
    @property
    def room_number(self): return self.__room_number
    @property
    def price_per_night(self): return self.__price_per_night
    @property
    def hotel(self): return self.__hotel
    @property
    def room_type(self): return self.__room_type

    def __repr__(self):
        return f"<Room {self.room_number}, {self.room_type.description}, {self.price_per_night:.2f} CHF>"

    @classmethod
    def from_row(cls, row, hotel: Hotel, room_type: RoomType):
        return cls(row[0], row[1], row[2], hotel, room_type)

    def to_dict(self):
        return {
            "room_id": self.room_id,
            "room_number": self.room_number,
            "price_per_night": self.price_per_night,
            "hotel": self.hotel.to_dict(),
            "room_type": self.room_type.to_dict()
        }
