from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        sql = "INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)"
        params = (street, city, zip_code)
        last_row_id, _ = self.execute(sql, params)
        return model.Address(last_row_id, street, city, zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        sql = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        result = self.fetchone(sql, (address_id,))
        return model.Address(*result) if result else None
