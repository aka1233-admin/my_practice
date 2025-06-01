# Copyright (c) 2025, Akanksha and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	
	columns = [
		{
			"fieldname": "airline",
			"label": "Airline",
			"fieldtype": "Data"
		},
		{
			"fieldname": "total_revenue",
			"label": "Total Revenue",
			"fieldtype": "Currency",
			"options": "AED"
		}

	]

	data = frappe.get_all(
		"Airplane Ticket",
		fields=["SUM(total_amount) AS total_revenue", "airline"],
		filters={"docstatus": 1},
		group_by="airline"
	)
	summary=[
    {
    }
]

	return columns, data
