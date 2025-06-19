from model.invoice import Invoice
from model.booking import Booking
from data_access.base_data_access import BaseDataAccess
from data_access.booking_DAL import BookingDataAccess

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.booking_dal = BookingDataAccess(db_path)

    def read_invoice_by_id(self, invoice_id: int) -> Invoice | None:
        #simpleexplanation: Fetches invoice with linked booking and issue date
        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice WHERE invoice_id = ?
        """
        row = self.fetchone(sql, (invoice_id,))
        if row:
            booking = self.booking_dal.read_booking_by_id(row[1])
            issue_date = row[2]
            # Fix: decode bytes to string if necessary
            if isinstance(issue_date, bytes):
                issue_date = issue_date.decode("utf-8")
            return Invoice(row[0], booking, issue_date, row[3])
        return None

    def create_invoice(self, booking: Booking, total_amount: float) -> Invoice:
        #simpleexplanation: Inserts a new invoice, retrieves the issue date, and returns an Invoice object
        sql = """
        INSERT INTO Invoice (booking_id, total_amount)
        VALUES (?, ?)
        """
        params = (booking.booking_id, total_amount)
        invoice_id, _ = self.execute(sql, params)

        # Fetch the issue date for the new invoice
        sql_date = "SELECT issue_date FROM Invoice WHERE invoice_id = ?"
        row = self.fetchone(sql_date, (invoice_id,))
        issue_date = row[0]
        if isinstance(issue_date, bytes):
            issue_date = issue_date.decode("utf-8")

        return Invoice(invoice_id, booking, issue_date, total_amount)
