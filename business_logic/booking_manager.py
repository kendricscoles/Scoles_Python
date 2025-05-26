import os

import model
import data_access

class Booking:
    def __init__(self) -> None:
        self.__booking_dal = data_access.BookingDAL()

    def create_booking(self, check_in_date, check_out_date, is_cancelled: bool, total_amount: float, guest: model.Guest, room: model.Room) -> model.Booking:
        return self.__booking_dal.create_new_booking(check_in_date, check_out_date, is_cancelled, total_amount, guest, room)

    def read_booking(self, booking_id: int) -> model.Booking:
        return self.__booking_dal.read_booking_by_id(booking_id)
