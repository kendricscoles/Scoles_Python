from model.invoice import Invoice
from model.booking import Booking
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
            issue_date = row[2].decode("utf-8") if isinstance(row[2], bytes) else row[2]
            return Invoice(row[0], booking, issue_date, row[3])
        return None

    def create_invoice(self, booking: Booking, total_amount: float) -> Invoice:
        sql = """
        INSERT INTO Invoice (booking_id, total_amount)
        VALUES (?, ?)
        """
        invoice_id, _ = self.execute(sql, (booking.booking_id, total_amount))

        row = self.fetchone("SELECT issue_date FROM Invoice WHERE invoice_id = ?", (invoice_id,))
        issue_date = row[0].decode("utf-8") if isinstance(row[0], bytes) else row[0]

        return Invoice(invoice_id, booking, issue_date, total_amount)
