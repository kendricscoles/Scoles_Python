class Address:
    def __init__(self) -> None:
        self.__address_dal = data_access.AddressDAL()

    def create_address(self, street: str, city: str, zip: str) -> model.Address:
        return self.__address_dal.create_new_address(street, city, zip)

    def read_address(self, address_id: int) -> model.Address:
        return self.__address_dal.read_address_by_id(address_id)
