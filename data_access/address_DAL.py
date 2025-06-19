from model.address import Address
from data_access.base_data_access import BaseDataAccess

class AddressDataAccess(BaseDataAccess):
    def create_address(self, street: str, city: str, postal_code: str, country: str = "Switzerland") -> Address:
        sql = "INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)"
        params = (street, city, postal_code)
        last_id, _ = self.execute(sql, params)
        return Address(last_id, street, city, postal_code, country)

    def read_address_by_id(self, address_id: int) -> Address | None:
        sql = "SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?"
        row = self.fetchone(sql, (address_id,))
        return Address.from_row(row) if row else None

    def read_all_addresses(self) -> list[Address]:
        sql = "SELECT address_id, street, city, zip_code FROM Address"
        rows = self.fetchall(sql)
        return [Address.from_row(row) for row in rows]
