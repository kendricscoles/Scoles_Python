class RoomType:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        if not room_type_id or not isinstance(room_type_id, int):
            raise ValueError("room_type_id must be an integer")
        if not description or not isinstance(description, str):
            raise ValueError("description must be a string")
        if not isinstance(max_guests, int):
            raise ValueError("max_guests must be an integer")

        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def room_type_id(self): return self.__room_type_id

    @property
    def description(self): return self.__description
    @description.setter
    def description(self, value): self.__description = value

    @property
    def max_guests(self): return self.__max_guests
    @max_guests.setter
    def max_guests(self, value): self.__max_guests = value
