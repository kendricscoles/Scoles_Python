from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        
    def search_hotels(self, city=None, min_stars=None, max_guests=None, check_in_date=None, check_out_date=None) -> pd.DataFrame:
        query = """
        SELECT h.name AS Hotel_Name, h.stars AS Stars, a.street AS Street, a.city AS City, a.zip_code AS Zip_Code
        FROM Hotel h
        JOIN Address a ON h.address_id = a.address_id
        WHERE 1=1
        """

        if city:
            query += f" AND a.city = '{city}'"
        if min_stars:
            query += f" AND h.stars >= {min_stars}"
        if max_guests:
            query += f"""
            AND h.hotel_id IN (
                SELECT r.hotel_id
                FROM Room r
                JOIN Room_Type rt ON r.type_id = rt.type_id
                WHERE rt.max_guests >= {max_guests}
            )
            """
        if check_in_date and check_out_date:
            query += f"""
            AND h.hotel_id IN (
                SELECT r.hotel_id
                FROM Room r
                WHERE r.room_id NOT IN (
                    SELECT b.room_id
                    FROM Booking b
                    WHERE (
                        (b.check_in_date < '{check_out_date}') AND (b.check_out_date > '{check_in_date}')
                    ) AND b.is_cancelled = 0
                )
            )
            """

        df = pd.read_sql_query(query, conn)
        return df
