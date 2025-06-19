from model.room import Room
from model.hotel import Hotel
from model.room_type import RoomType
from data_access.base_data_access import BaseDataAccess
from data_access.hotel_DAL import HotelDataAccess
from data_access.room_type_DAL import RoomTypeDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.hotel_dal = HotelDataAccess(db_path)
        self.room_type_dal = RoomTypeDataAccess(db_path)

    def read_room_by_id(self, room_id: int) -> Room | None:
        sql = "SELECT room_id, hotel_id, room_number, type_id, price_per_night FROM Room WHERE room_id = ?"
        row = self.fetchone(sql, (room_id,))
        if row:
            hotel = self.hotel_dal.read_hotel_by_id(row[1])
            room_type = self.room_type_dal.read_room_type_by_id(row[3])
            return Room(row[0], row[2], row[4], hotel, room_type)
        return None
