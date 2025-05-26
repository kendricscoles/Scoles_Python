from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id: int, booking: Booking, issue_date: date, total_amount: float):
        if not invoice_id or not isinstance(invoice_id, int):
            raise ValueError("invoice_id must be an integer")
        if not isinstance(issue_date, date):
            raise ValueError("issue_date must be a date")
        if not isinstance(total_amount, (int, float)):
            raise ValueError("total_amount must be a number")

        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__issue_date = issue_date
        self.__total_amount = float(total_amount)

    @property
    def invoice_id(self): return self.__invoice_id

    @property
    def booking(self): return self.__booking
    @booking.setter
    def booking(self, value): self.__booking = value

    @property
    def issue_date(self): return self.__issue_date
    @issue_date.setter
    def issue_date(self, value): self.__issue_date = value

    @property
    def total_amount(self): return self.__total_amount
    @total_amount.setter
    def total_amount(self, value): self.__total_amount = float(value)
