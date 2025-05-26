import os

import model
import data_access

class RoomType:
    def __init__(self) -> None:
        self.__room_type_dal = data_access.RoomTypeDAL()

    def create_room_type(self, description: str, max_guests: int) -> model.RoomType:
        return self.__room_type_dal.create_new_room_type(description, max_guests)

    def read_room_type(self, room_type_id: int) -> model.RoomType:
        return self.__room_type_dal.read_room_type_by_id(room_type_id)
