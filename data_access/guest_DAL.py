from model.guest import Guest
from model.address import Address
from data_access.base_data_access import BaseDataAccess
from data_access.address_DAL import AddressDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.address_dal = AddressDataAccess(db_path)

    def read_guest_by_id(self, guest_id: int) -> Guest | None:
        sql = """
        SELECT g.guest_id, g.first_name, g.last_name, g.email, a.address_id, a.street, a.city, a.zip_code
        FROM Guest g
        LEFT JOIN Address a ON g.address_id = a.address_id
        WHERE g.guest_id = ?
        """
        row = self.fetchone(sql, (guest_id,))
        if row:
            address = Address.from_row(row[4:]) if row[4] else None
            return Guest(row[0], row[1], row[2], row[3], address)
        return None

    def create_guest(self, first_name: str, last_name: str, email: str, address_id: int = None) -> Guest:
        sql = "INSERT INTO Guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"
        params = (first_name, last_name, email, address_id)
        last_id, _ = self.execute(sql, params)
        address = self.address_dal.read_address_by_id(address_id) if address_id else None
        return Guest(last_id, first_name, last_name, email, address)
