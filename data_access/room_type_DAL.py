from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_room_type(self, description: str, max_guests: int) -> model.RoomType:
        sql = "INSERT INTO Room_Type (description, max_guests) VALUES (?, ?)"
        params = (description, max_guests)
        last_row_id, _ = self.execute(sql, params)
        return model.RoomType(last_row_id, description, max_guests)

    def read_room_type_by_id(self, type_id: int) -> model.RoomType | None:
        sql = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        result = self.fetchone(sql, (type_id,))
        if result:
            return model.RoomType(*result)
        return None

    def read_all_room_types(self) -> list[model.RoomType]:
        sql = "SELECT type_id, description, max_guests FROM Room_Type"
        rows = self.fetchall(sql)
        return [model.RoomType(*row) for row in rows]

    def update_room_type(self, room_type: model.RoomType) -> int:
        sql = "UPDATE Room_Type SET description = ?, max_guests = ? WHERE type_id = ?"
        params = (room_type.description, room_type.max_guests, room_type.room_type_id)
        _, row_count = self.execute(sql, params)
        return row_count

    def delete_room_type(self, room_type: model.RoomType) -> int:
        sql = "DELETE FROM Room_Type WHERE type_id = ?"
        _, row_count = self.execute(sql, (room_type.room_type_id,))
        return row_count
