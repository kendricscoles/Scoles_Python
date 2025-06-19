from model.guest import Guest
from model.room import Room

class Booking:
    def __init__(self, booking_id: int, guest: Guest, room: Room,
                 check_in: str, check_out: str, is_cancelled: bool = False, total_amount: float = 0.0):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount

    @property
    def booking_id(self): return self.__booking_id
    @property
    def guest(self): return self.__guest
    @property
    def room(self): return self.__room
    @property
    def check_in(self): return self.__check_in
    @property
    def check_out(self): return self.__check_out
    @property
    def is_cancelled(self): return self.__is_cancelled
    @property
    def total_amount(self): return self.__total_amount

    def __repr__(self):
        return f"<Booking #{self.booking_id} | {self.check_in} - {self.check_out}>"

    @classmethod
    def from_row(cls, row, guest: Guest, room: Room):
        return cls(*row[:6], guest=guest, room=room)

    def to_dict(self):
        return {
            "booking_id": self.booking_id,
            "guest": self.guest.to_dict(),
            "room": self.room.to_dict(),
            "check_in": self.check_in,
            "check_out": self.check_out,
            "is_cancelled": self.is_cancelled,
            "total_amount": self.total_amount
        }
