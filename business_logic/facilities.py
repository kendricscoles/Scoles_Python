import os

import model
import data_access

class Facility:
    def __init__(self) -> None:
        self.__facility_dal = data_access.FacilityDAL()

    def create_facility(self, facility_name: str) -> model.Facility:
        return self.__facility_dal.create_new_facility(facility_name)

    def read_facility(self, facility_id: int) -> model.Facility:
        return self.__facility_dal.read_facility_by_id(facility_id)
