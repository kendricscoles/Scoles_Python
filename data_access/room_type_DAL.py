from model.room_type import RoomType
from data_access.base_data_access import BaseDataAccess

class RoomTypeDataAccess(BaseDataAccess):
    def read_room_type_by_id(self, type_id: int) -> RoomType | None:
        sql = "SELECT type_id, description, max_guests FROM Room_Type WHERE type_id = ?"
        row = self.fetchone(sql, (type_id,))
        return RoomType.from_row(row) if row else None
