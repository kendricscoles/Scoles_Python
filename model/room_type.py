class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def type_id(self): return self.__type_id
    @property
    def description(self): return self.__description
    @property
    def max_guests(self): return self.__max_guests

    def __repr__(self):
        return f"<RoomType {self.description} (max {self.max_guests} guests)>"

    @classmethod
    def from_row(cls, row):
        return cls(*row)

    def to_dict(self):
        return {
            "type_id": self.type_id,
            "description": self.description,
            "max_guests": self.max_guests
        }
