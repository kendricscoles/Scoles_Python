from __future__ import annotations
import model
from data_access.base_data_access import BaseDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_invoice(self, booking: model.Booking, issue_date: str, total_amount: float) -> model.Invoice:
        sql = "INSERT INTO Invoice (booking_id, issue_date, total_amount) VALUES (?, ?, ?)"
        params = (booking.booking_id, issue_date, total_amount)
        last_row_id, _ = self.execute(sql, params)
        return model.Invoice(last_row_id, booking, issue_date, total_amount)

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        sql = "SELECT invoice_id, booking_id, issue_date, total_amount FROM Invoice WHERE invoice_id = ?"
        result = self.fetchone(sql, (invoice_id,))
        if result:
            iid, bid, issue_date, total = result
            return model.Invoice(iid, model.Booking(bid), issue_date, total)
        return None
