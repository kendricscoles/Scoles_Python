from model.booking import Booking
from model.guest import Guest
from model.room import Room
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

    def create_booking(self, guest: Guest, room: Room, check_in: str, check_out: str, total_amount: float) -> Booking:
        #simpleexplanation: Inserts a new booking and returns a Booking object
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, total_amount)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (guest.guest_id, room.room_id, check_in, check_out, total_amount)
        booking_id, _ = self.execute(sql, params)
        return Booking(booking_id, guest, room, check_in, check_out, False, total_amount)
