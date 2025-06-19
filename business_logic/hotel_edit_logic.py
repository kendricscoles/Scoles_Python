from model.hotel import Hotel
from model.address import Address
from data_access.hotel_DAL import HotelDataAccess
from data_access.address_DAL import AddressDataAccess

DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

#simpleexplanation: Adds a new hotel to the database
def create_hotel(name: str, stars: int, address_id: int) -> Hotel:
    hotel_dal = HotelDataAccess(DB_PATH)
    return hotel_dal.create_hotel(name, stars, address_id)

#simpleexplanation: Deletes a hotel from the database by ID
def delete_hotel_by_id(hotel_id: int) -> bool:
    hotel_dal = HotelDataAccess(DB_PATH)
    return hotel_dal.delete_hotel_by_id(hotel_id)

#simpleexplanation: Updates the name of a hotel
def update_hotel_name(hotel_id: int, new_name: str) -> bool:
    hotel_dal = HotelDataAccess(DB_PATH)
    return hotel_dal.update_hotel_name(hotel_id, new_name)

#simpleexplanation: Updates the star rating of a hotel
def update_hotel_stars(hotel_id: int, new_stars: int) -> bool:
    hotel_dal = HotelDataAccess(DB_PATH)
    return hotel_dal.update_hotel_stars(hotel_id, new_stars)

#simpleexplanation: Updates the address of a hotel
def update_hotel_address(hotel_id: int, new_address_id: int) -> bool:
    hotel_dal = HotelDataAccess(DB_PATH)
    return hotel_dal.update_hotel_address(hotel_id, new_address_id)
