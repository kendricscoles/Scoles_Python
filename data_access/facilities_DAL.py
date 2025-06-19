from model.facility import Facility
from data_access.base_data_access import BaseDataAccess

class FacilityDataAccess(BaseDataAccess):
    def read_all_facilities(self) -> list[Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities"
        rows = self.fetchall(sql)
        return [Facility(row[0], row[1]) for row in rows]
