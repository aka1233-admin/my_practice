# Copyright (c) 2025, AKanksha and contributors
# For license information, please see license.txt

import frappe
from frappe import enqueue
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFligh(WebsiteGenerator):
	def on_update(self):
		if self.has_value_changed("gate_number"):
			enqueue(
				"airplane_shop_management.path.to.update_gate_number_in_tickets",
				queue="default",
				kwargs={"flight_date": self.date, "new_gate": self.gate_number}
			)

	

	def update_gate_number_in_tickets(flight_date, new_gate):
		tickets = frappe.db.get_all('Airplane Ticket', filters={'date': flight_date})
		for ticket in tickets:
			frappe.db.set_value('Airplane Ticket', ticket['name'], 'gate_number', new_gate)
