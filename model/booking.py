from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
   from model.guest import Guest
   from model.room import Room

class Booking:
   def __init__(self, booking_id: int, check_in_date: date, check_out_date: date, guest: Guest, room: Room):
       if not booking_id or not isinstance(booking_id, int):
           raise ValueError("booking_id must be an integer")
       if not isinstance(check_in_date, date):
           raise ValueError("check_in_date must be a date object")
       if not isinstance(check_out_date, date):
           raise ValueError("check_out_date must be a date object")
       if check_in_date >= check_out_date:
           raise ValueError("check_in_date must be before check_out_date")
       
       self.__booking_id = booking_id
       self.__check_in_date = check_in_date
       self.__check_out_date = check_out_date
       self.__guest = guest
       self.__room = room
       
   @property
   def booking_id(self): return self.__booking_id

   @property
   def check_in_date(self): return self.__check_in_date
   @check_in_date.setter
   def check_in_date(self, value): self.__check_in_date = value

   @property
   def check_out_date(self): return self.__check_out_date
   @check_out_date.setter
   def check_out_date(self, value): self.__check_out_date = value

   @property
   def guest(self): return self.__guest
   @guest.setter
   def guest(self, value): self.__guest = value

   @property
   def room(self): return self.__room
   @room.setter
   def room(self, value): self.__room = value
