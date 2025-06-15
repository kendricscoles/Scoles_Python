from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room(self, hotel: model.Hotel, room_number: str, room_type: model.RoomType, price_per_night: float) -> model.Room:
        sql = "INSERT INTO Room (hotel_id, room_number, type_id, price_per_night) VALUES (?, ?, ?, ?)"
        params = (hotel.hotel_id, room_number, room_type.room_type_id, price_per_night)
        last_row_id, _ = self.execute(sql, params)
        return model.Room(last_row_id, room_number, price_per_night, room_type, hotel)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        sql = "SELECT room_id, room_number, price_per_night, type_id, hotel_id FROM Room WHERE room_id = ?"
        result = self.fetchone(sql, (room_id,))
        if result:
            room_id, room_number, price_per_night, type_id, hotel_id = result
            return model.Room(room_id, room_number, price_per_night, model.RoomType(type_id), model.Hotel(hotel_id))
        return None

    def read_all_rooms(self) -> list[model.Room]:
        sql = "SELECT room_id, room_number, price_per_night, type_id, hotel_id FROM Room"
        rows = self.fetchall(sql)
        return [model.Room(rid, rn, price, model.RoomType(tid), model.Hotel(hid))
                for rid, rn, price, tid, hid in rows]

    def update_room(self, room: model.Room) -> int:
        sql = "UPDATE Room SET hotel_id = ?, room_number = ?, type_id = ?, price_per_night = ? WHERE room_id = ?"
        params = (room.hotel.hotel_id, room.room_no, room.room_type.room_type_id, room.price_per_night, room.room_id)
        _, row_count = self.execute(sql, params)
        return row_count

    def delete_room(self, room: model.Room) -> int:
        sql = "DELETE FROM Room WHERE room_id = ?"
        _, row_count = self.execute(sql, (room.room_id,))
        return row_count
