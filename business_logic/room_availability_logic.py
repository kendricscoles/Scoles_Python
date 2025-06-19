from model.room import Room
from typing import List

DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

#simpleexplanation: Returns available Room objects for a hotel in a given date range
def get_available_rooms(hotel_id: int, check_in: str, check_out: str) -> List[Room]:
    from data_access.base_data_access import BaseDataAccess
    from data_access.room_DAL import RoomDataAccess
    from data_access.room_type_DAL import RoomTypeDataAccess
    from data_access.hotel_DAL import HotelDataAccess

    db = BaseDataAccess(DB_PATH)
    room_dal = RoomDataAccess(DB_PATH)
    room_type_dal = RoomTypeDataAccess(DB_PATH)
    hotel_dal = HotelDataAccess(DB_PATH)

    hotel = hotel_dal.read_hotel_by_id(hotel_id)
    if not hotel:
        return []

    sql = """
    SELECT room_id, room_number, type_id, price_per_night
    FROM Room
    WHERE hotel_id = ?
    AND room_id NOT IN (
        SELECT room_id FROM Booking
        WHERE is_cancelled = 0
        AND (check_in_date < ? AND check_out_date > ?)
    )
    """
    rows = db.fetchall(sql, (hotel_id, check_out, check_in))

    available_rooms = []
    for row in rows:
        room_id, room_no, type_id, price = row
        room_type = room_type_dal.read_room_type_by_id(type_id)
        if room_type:
            room = Room(room_id, room_no, price, hotel, room_type)
            available_rooms.append(room)

    return available_rooms

#simpleexplanation: Displays info about available rooms including type, max guests, nightly and total price, and facilities
def display_room_details(rooms: List[Room], check_in: str, check_out: str):
    from datetime import datetime
    from data_access.base_data_access import BaseDataAccess

    db = BaseDataAccess(DB_PATH)

    def nights_between(start, end):
        s = datetime.strptime(start, "%Y-%m-%d")
        e = datetime.strptime(end, "%Y-%m-%d")
        return (e - s).days

    nights = nights_between(check_in, check_out)

    for room in rooms:
        sql = """
        SELECT f.facility_name
        FROM Facilities f
        JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
        WHERE rf.room_id = ?
        """
        facilities = db.fetchall(sql, (room.room_id,))
        fac_list = [f[0] for f in facilities] if facilities else ["(None)"]

        total_price = room.price_per_night * nights

        print(
            f"Room {room.room_number} | {room.room_type.description} | max {room.room_type.max_guests} guests | "
            f"{room.price_per_night:.2f} CHF/night | {total_price:.2f} CHF total | "
            f"Facilities: {', '.join(fac_list)}"
        )
