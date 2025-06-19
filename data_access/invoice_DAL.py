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
            return Invoice(row[0], booking, row[2], row[3])
        return None

    def create_invoice(self, booking: Booking, total_amount: float) -> Invoice:
        #simpleexplanation: Inserts a new invoice linked to a booking
        sql = """
        INSERT INTO Invoice (booking_id, total_amount)
        VALUES (?, ?)
        """
        params = (booking.booking_id, total_amount)
        invoice_id, _ = self.execute(sql, params)

        # Fetch issue_date from DB to include in Invoice object
        row = self.fetchone(
            "SELECT issue_date FROM Invoice WHERE invoice_id = ?", (invoice_id,)
        )
        issue_date = row[0] if row else "(unknown)"

        return Invoice(invoice_id, booking, issue_date, total_amount)
