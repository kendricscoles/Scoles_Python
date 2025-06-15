from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_hotel(self, name: str, stars: int, address: model.Address = None) -> model.Hotel:
        sql = """
        INSERT INTO Hotel (name, stars, address_id)
        VALUES (?, ?, ?)
        """
        params = (
            name,
            stars,
            address.address_id if address else None,
        )

        last_row_id, row_count = self.execute(sql, params)
        return model.Hotel(last_row_id, name, stars, address)

    def read_hotel_by_id(self, hotel_id: int) -> model.Hotel | None:
        sql = """
        SELECT hotel_id, name, stars, address_id
        FROM Hotel
        WHERE hotel_id = ?
        """
        result = self.fetchone(sql, (hotel_id,))
        if result:
            hotel_id, name, stars, address_id = result
            address = model.Address(address_id) if address_id else None
            return model.Hotel(hotel_id, name, stars, address)
        return None

    def read_all_hotels(self) -> list[model.Hotel]:
        sql = """
        SELECT hotel_id, name, stars, address_id
        FROM Hotel
        """
        rows = self.fetchall(sql)
        return [
            model.Hotel(hotel_id, name, stars, model.Address(address_id) if address_id else None)
            for hotel_id, name, stars, address_id in rows
        ]

    def update_hotel(self, hotel: model.Hotel) -> int:
        sql = """
        UPDATE Hotel
        SET name = ?, stars = ?, address_id = ?
        WHERE hotel_id = ?
        """
        params = (
            hotel.name,
            hotel.stars,
            hotel.address.address_id if hotel.address else None,
            hotel.hotel_id,
        )
        _, row_count = self.execute(sql, params)
        return row_count

    def delete_hotel(self, hotel: model.Hotel) -> int:
        sql = """
        DELETE FROM Hotel
        WHERE hotel_id = ?
        """
        _, row_count = self.execute(sql, (hotel.hotel_id,))
        return row_count
