DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

#simpleexplanation: Cancels an existing booking by ID
def cancel_booking(booking_id: int) -> bool:
    from data_access.booking_DAL import BookingDataAccess
    booking_dal = BookingDataAccess(DB_PATH)
    return booking_dal.cancel_booking_by_id(booking_id)
