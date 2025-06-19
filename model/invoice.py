from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id: int, booking: Booking, issue_date: str, total_amount: float):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__issue_date = issue_date
        self.__total_amount = total_amount

    @property
    def invoice_id(self): return self.__invoice_id
    @property
    def booking(self): return self.__booking
    @property
    def issue_date(self): return self.__issue_date
    @property
    def total_amount(self): return self.__total_amount

    def __repr__(self):
        return f"<Invoice #{self.invoice_id} | CHF {self.total_amount:.2f}>"

    @classmethod
    def from_row(cls, row, booking: Booking):
        invoice_id, _booking_id, issue_date, total_amount = row
        return cls(invoice_id, booking, issue_date, total_amount)

    def to_dict(self):
        return {
            "invoice_id": self.invoice_id,
            "booking": self.booking.to_dict(),
            "issue_date": self.issue_date,
            "total_amount": self.total_amount
        }
