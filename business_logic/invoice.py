import os

import model
import data_access

class Invoice:
    def __init__(self) -> None:
        self.__invoice_dal = data_access.InvoiceDAL()

    def create_invoice(self, issue_date, total_amount: float, booking: model.Booking) -> model.Invoice:
        return self.__invoice_dal.create_new_invoice(issue_date, total_amount, booking)

    def read_invoice(self, invoice_id: int) -> model.Invoice:
        return self.__invoice_dal.read_invoice_by_id(invoice_id)
