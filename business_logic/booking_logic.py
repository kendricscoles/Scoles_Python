from model.booking import Booking
from model.guest import Guest
from model.room import Room

DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

#simpleexplanation: Creates a new booking if the room is available
def create_booking(guest_id: int, room_id: int, check_in: str, check_out: str) -> Booking | None:
    from data_access.booking_DAL import BookingDataAccess
    from data_access.guest_DAL import GuestDataAccess
    from data_access.room_DAL import RoomDataAccess

    guest_dal = GuestDataAccess(DB_PATH)
    room_dal = RoomDataAccess(DB_PATH)
    booking_dal = BookingDataAccess(DB_PATH)

    guest = guest_dal.read_guest_by_id(guest_id)
    room = room_dal.read_room_by_id(room_id)

    if not guest or not room:
        print("⚠️ Guest or Room not found.")
        return None

    # Check if room is already booked
    sql = """
    SELECT booking_id FROM Booking
    WHERE room_id = ?
    AND is_cancelled = 0
    AND (check_in_date < ? AND check_out_date > ?)
    """
    overlaps = booking_dal.fetchall(sql, (room_id, check_out, check_in))
    if overlaps:
        print("⚠️ Room is not available during selected dates.")
        return None

    # Calculate total
    from datetime import datetime
    nights = (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
    total = nights * room.price_per_night

    booking = booking_dal.create_booking(guest, room, check_in, check_out, total)
    return booking
