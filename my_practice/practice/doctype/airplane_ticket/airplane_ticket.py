# Copyright (c) 2025, Akanksha and contributors
# For license information, please see license.txt
import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        total=sum([row.amount for row in self.payment_details])
        if total != self.total_amount:
            frappe.throw("Sum of all the payments amount must be equal the total amount and the ticket amount")
        for row in self.payment_details:
            if row.due_date < today():
                frappe.throw(f"due date {row.due_date} must be today or future date")

    def on_submit(self):
        if self.reference_doctype == "Airplane Ticket":
            ticket = frappe.get_doc("Airplane Ticket", self.reference_name)
            for schedule in ticket.payment_details:
                if schedule.status != "Paid" and schedule.amount == self.paid_amount:
                    schedule.status = "Paid"
                    schedule.reference = self.name
            ticket.save()

    def on_submit(self):
        for payment in self.payment_details:
            if not payment.status:
                payment.status = "Pending"

    def validate(self):
        # -----------------------
        # 1. Capacity Check
        # -----------------------
        if not self.flight:
            return  # No flight selected

        flight_doc = frappe.get_doc("Airplane Fligh", self.flight)

        if not flight_doc.airplane:
            return  # No airplane assigned to flight

        airplane_doc = frappe.get_doc("Airplane", flight_doc.airplane)
        capacity = airplane_doc.capacity or 0

        count = frappe.db.count("Airplane Ticket", {
            "flight": self.flight,
            "docstatus": ("<", 2),
            "name": ("!=", self.name)
        })

        if count >= capacity:
            frappe.throw(f"Cannot create more tickets: Flight '{self.flight}' has reached maximum capacity ({capacity}).")

        # -----------------------
        # 2. Flight Price & Total Amount
        # -----------------------
        if not self.flight_price:
            frappe.throw("Please provide price")

        self.remove_duplicate_add_ons()

        # Calculate total amount
        t_amount = sum(item.amount for item in self.add_ons)
        self.total_amount = t_amount * self.flight_price

    def before_insert(self):
        # Generate a random seat like 89E
        seat_number = f"{random.randint(1, 99)}{random.choice('ABCDE')}"
        self.seat = seat_number

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("You can only submit the document when the status is boarded")

    def remove_duplicate_add_ons(self):
        seen = set()
        unique_add_ons = []

        for item in self.add_ons:
            if item.item not in seen:
                seen.add(item.item)
                unique_add_ons.append(item)

        self.set("add_ons", [])
        for item in unique_add_ons:
            self.append("add_ons", item)

    
