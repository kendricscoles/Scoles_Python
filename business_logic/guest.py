import os

import model
import data_access

class Guest:
    def __init__(self) -> None:
        self.__guest_dal = data_access.GuestDAL()

    def create_guest(self, first_name: str, last_name: str, email: str, address: model.Address) -> model.Guest:
        return self.__guest_dal.create_new_guest(first_name, last_name, email, address)

    def read_guest(self, guest_id: int) -> model.Guest:
        return self.__guest_dal.read_guest_by_id(guest_id)
