from model.hotel import Hotel
from typing import List

#  Deepnote-safe absolute DB path
DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

#simpleexplanation: Filters all hotels based on city name
def get_hotels_by_city(city: str) -> List[Hotel]:
    from data_access.hotel_DAL import HotelDataAccess
    dal = HotelDataAccess(DB_PATH)
    all_hotels = dal.read_all_hotels()
    return [h for h in all_hotels if h.address.city.lower() == city.lower()]

#simpleexplanation: Filters hotels in a city that have at least the given star rating
def get_hotels_by_city_and_min_stars(city: str, min_stars: int) -> List[Hotel]:
    hotels = get_hotels_by_city(city)
    return [h for h in hotels if h.stars >= min_stars]

#simpleexplanation: Filters hotels that have rooms for at least the given number of guests
def filter_hotels_by_guest_capacity(hotels: List[Hotel], guests: int) -> List[Hotel]:
    from data_access.room_DAL import RoomDataAccess
    from data_access.room_type_DAL import RoomTypeDataAccess
    room_dal = RoomDataAccess(DB_PATH)
    room_type_dal = RoomTypeDataAccess(DB_PATH)
    valid_hotels = []

    for hotel in hotels:
        sql = "SELECT type_id FROM Room WHERE hotel_id = ?"
        rows = room_dal.fetchall(sql, (hotel.hotel_id,))
        for row in rows:
            room_type = room_type_dal.read_room_type_by_id(row[0])
            if room_type and room_type.max_guests >= guests:
                valid_hotels.append(hotel)
                break
    return valid_hotels

#simpleexplanation: Filters hotels that have at least one available room in the date range
def filter_hotels_by_availability(hotels: List[Hotel], check_in: str, check_out: str) -> List[Hotel]:
    from data_access.base_data_access import BaseDataAccess
    base = BaseDataAccess(DB_PATH)
    available_hotels = []

    for hotel in hotels:
        sql = """
        SELECT r.room_id
        FROM Room r
        WHERE r.hotel_id = ?
        AND r.room_id NOT IN (
            SELECT room_id FROM Booking
            WHERE is_cancelled = 0
            AND (check_in_date < ? AND check_out_date > ?)
        )
        """
        result = base.fetchall(sql, (hotel.hotel_id, check_out, check_in))
        if result:
            available_hotels.append(hotel)
    return available_hotels

#simpleexplanation: Combines all filters to find matching hotels
def search_hotels_combined(city: str, min_stars: int, guests: int, check_in: str, check_out: str) -> List[Hotel]:
    hotels = get_hotels_by_city_and_min_stars(city, min_stars)
    hotels = filter_hotels_by_guest_capacity(hotels, guests)
    hotels = filter_hotels_by_availability(hotels, check_in, check_out)
    return hotels

#simpleexplanation: Displays basic hotel info
def display_hotel_info(hotels: List[Hotel]):
    for h in hotels:
        print(f"{h.name} | {h.address.street}, {h.address.city} | {h.stars}★")
