from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
   from model.address import Address

class Guest:
   def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, phone: str, address: Optional[Address] = None):
       if not guest_id or not isinstance(guest_id, int):
           raise ValueError("guest_id must be an integer")
       if not first_name or not isinstance(first_name, str):
           raise ValueError("first_name must be a string")
       if not last_name or not isinstance(last_name, str):
           raise ValueError("last_name must be a string")
       if not email or not isinstance(email, str):
           raise ValueError("email must be a string")
       if not phone or not isinstance(phone, str):
           raise ValueError("phone must be a string")
       
       self.__guest_id = guest_id
       self.__first_name = first_name
       self.__last_name = last_name
       self.__email = email
       self.__phone = phone
       self.__address = address
       
   @property
   def guest_id(self): return self.__guest_id

   @property
   def first_name(self): return self.__first_name
   @first_name.setter
   def first_name(self, value): self.__first_name = value

   @property
   def last_name(self): return self.__last_name
   @last_name.setter
   def last_name(self, value): self.__last_name = value

   @property
   def email(self): return self.__email
   @email.setter
   def email(self, value): self.__email = value

   @property
   def phone(self): return self.__phone
   @phone.setter
   def phone(self, value): self.__phone = value

   @property
   def address(self): return self.__address
   @address.setter
   def address(self, value): self.__address = value
