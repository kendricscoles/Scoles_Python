from model.invoice import Invoice
from model.booking import Booking

DB_PATH = "/root/work/Scoles_Python/database/hotel_reservation_sample.db"

def create_invoice(booking_id: int) -> Invoice | None:
    from data_access.booking_DAL import BookingDataAccess
    from data_access.invoice_DAL import InvoiceDataAccess

    booking_dal = BookingDataAccess(DB_PATH)
    invoice_dal = InvoiceDataAccess(DB_PATH)

    booking = booking_dal.read_booking_by_id(booking_id)
    if not booking:
        print("❌ Booking not found.")
        return None

    return invoice_dal.create_invoice(booking, booking.total_amount)

def display_invoice(invoice: Invoice):
    print("📄 INVOICE")
    print(f"Invoice ID: {invoice.invoice_id}")
    print(f"Guest: {invoice.booking.guest.first_name} {invoice.booking.guest.last_name}")
    print(f"Room: {invoice.booking.room.room_number}")
    print(f"Stay: {invoice.booking.check_in} to {invoice.booking.check_out}")
    print(f"Total: CHF {invoice.total_amount:.2f}")
    print(f"Issue Date: {invoice.issue_date}")
