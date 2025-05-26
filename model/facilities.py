from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
   from model.hotel import Hotel

class Facility:
   def __init__(self, facility_id: int, name: str, description: str, hotel: Hotel):
       if not facility_id or not isinstance(facility_id, int):
           raise ValueError("facility_id must be an integer")
       if not name or not isinstance(name, str):
           raise ValueError("name must be a string")
       if not description or not isinstance(description, str):
           raise ValueError("description must be a string")
       
       self.__facility_id = facility_id
       self.__name = name
       self.__description = description
       self.__hotel = hotel
       
   @property
   def facility_id(self): return self.__facility_id

   @property
   def name(self): return self.__name
   @name.setter
   def name(self, value): self.__name = value

   @property
   def description(self): return self.__description
   @description.setter
   def description(self, value): self.__description = value

   @property
   def hotel(self): return self.__hotel
   @hotel.setter
   def hotel(self, value): self.__hotel = value
