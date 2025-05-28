# Copyright (c) 2025, AKanksha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
	def validate(self):
		if frappe.session.user != 'Administrator' and not frappe.has_role("Airport Authority Personnel"):
			if self.initial_audit_completed:
				frappe.throw("You are not allowed to mark the Initial Audit as completed.")

