import os

import model
import data_access

class Room:
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDAL()

    def create_room(self, room_no: str, price_per_night: float, room_type: model.RoomType, hotel: model.Hotel) -> model.Room:
        return self.__room_dal.create_new_room(room_no, price_per_night, room_type, hotel)

    def read_room(self, room_id: int) -> model.Room:
        return self.__room_dal.read_room_by_id(room_id)
