from model.hotel import Hotel
from model.address import Address
from data_access.base_data_access import BaseDataAccess
from data_access.address_DAL import AddressDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.address_dal = AddressDataAccess(db_path)

    def read_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE h.hotel_id = ?
        """
        row = self.fetchone(sql, (hotel_id,))
        if row:
            address = Address.from_row(row[3:])
            return Hotel(hotel_id=row[0], name=row[1], address=address, stars=row[2])
        return None

    def read_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        """
        rows = self.fetchall(sql)
        return [Hotel(row[0], row[1], Address.from_row(row[3:]), row[2]) for row in rows]

    def create_hotel(self, name: str, stars: int, address_id: int) -> Hotel:
    sql = "INSERT INTO Hotel (name, stars, address_id) VALUES (?, ?, ?)"
    params = (name, stars, address_id)
    hotel_id, _ = self.execute(sql, params)
    from model.address import Address
    return Hotel(hotel_id, name, Address(address_id, "", "", ""), stars)

    def delete_hotel_by_id(self, hotel_id: int) -> bool:
    sql = "DELETE FROM Hotel WHERE hotel_id = ?"
    _, rows = self.execute(sql, (hotel_id,))
    return rows > 0

    def update_hotel_name(self, hotel_id: int, new_name: str) -> bool:
    sql = "UPDATE Hotel SET name = ? WHERE hotel_id = ?"
    _, rows = self.execute(sql, (new_name, hotel_id))
    return rows > 0

    def update_hotel_stars(self, hotel_id: int, stars: int) -> bool:
    sql = "UPDATE Hotel SET stars = ? WHERE hotel_id = ?"
    _, rows = self.execute(sql, (stars, hotel_id))
    return rows > 0

    def update_hotel_address(self, hotel_id: int, address_id: int) -> bool:
    sql = "UPDATE Hotel SET address_id = ? WHERE hotel_id = ?"
    _, rows = self.execute(sql, (address_id, hotel_id))
    return rows > 0
