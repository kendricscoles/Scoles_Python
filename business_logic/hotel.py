class Hotel:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_dal.create_new_hotel(name, stars, address)

    def read_hotel(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_dal.read_hotel_by_id(hotel_id)
