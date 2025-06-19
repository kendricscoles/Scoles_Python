from model.invoice import Invoice
from data_access.base_data_access import BaseDataAccess
from data_access.booking_DAL import BookingDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.booking_dal = BookingDataAccess(db_path)

    def read_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        if row:
            booking = self.booking_dal.read_booking_by_id(row[1])
            return Invoice(row[0], booking, row[2], row[3])
        return None

    def create_invoice(self, booking: Booking, total_amount: float) -> Invoice:
    sql = """
    INSERT INTO Invoice (booking_id, total_amount)
    VALUES (?, ?)
    """
    params = (booking.booking_id, total_amount)
    invoice_id, _ = self.execute(sql, params)
    return Invoice(invoice_id, booking, issue_date="(now)", total_amount=total_amount)
