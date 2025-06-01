# Copyright (c) 2025, AKanksha and contributors
# For license information, please see license.txt

import frappe
from frappe import enqueue
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFligh(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
	def on_update(self):
		if self.has_value_changed("gate_number"):
			enqueue(
				"airplane_shop_management.path.to.update_gate_number_in_tickets",
				queue="default",
				kwargs={"flight_date": self.date, "new_gate": self.gate_number}
			)
			

	

	def update_ticket_gate_numbers(flight_name, gate_number):
		tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight_name}, fields=["name"])
		for ticket in tickets:
			ticket_doc = frappe.get_doc("Airplane Ticket", ticket.name)
			ticket_doc.gate_number = gate_number
			ticket_doc.save()