from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str, address: model.Address = None) -> model.Guest:
        sql = "INSERT INTO Guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
        params = (first_name, last_name, email, address.address_id if address else None)
        last_row_id, _ = self.execute(sql, params)
        return model.Guest(last_row_id, first_name, last_name, email, address)

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        sql = "SELECT guest_id, first_name, last_name, email, address_id FROM Guest WHERE guest_id = ?"
        result = self.fetchone(sql, (guest_id,))
        if result:
            guest_id, first, last, email, address_id = result
            address = model.Address(address_id) if address_id else None
            return model.Guest(guest_id, first, last, email, address)
        return None
