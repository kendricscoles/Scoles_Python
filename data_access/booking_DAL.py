from model.booking import Booking
from data_access.base_data_access import BaseDataAccess
from data_access.guest_DAL import GuestDataAccess
from data_access.room_DAL import RoomDataAccess

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.guest_dal = GuestDataAccess(db_path)
        self.room_dal = RoomDataAccess(db_path)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            guest = self.guest_dal.read_guest_by_id(row[1])
            room = self.room_dal.read_room_by_id(row[2])
            return Booking(row[0], guest, room, row[3], row[4], bool(row[5]), row[6])
        return None
