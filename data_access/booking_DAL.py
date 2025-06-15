from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking(self, guest: model.Guest, room: model.Room, check_in: str, check_out: str, is_cancelled: bool, total: float) -> model.Booking:
        sql = "INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount) VALUES (?, ?, ?, ?, ?, ?)"
        params = (guest.guest_id, room.room_id, check_in, check_out, is_cancelled, total)
        last_row_id, _ = self.execute(sql, params)
        return model.Booking(last_row_id, guest, room, check_in, check_out, is_cancelled, total)

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = "SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking WHERE booking_id = ?"
        result = self.fetchone(sql, (booking_id,))
        if result:
            bid, gid, rid, ci, co, cancelled, total = result
            return model.Booking(bid, model.Guest(gid), model.Room(rid), ci, co, cancelled, total)
        return None
