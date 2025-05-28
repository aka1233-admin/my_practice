import frappe
import random

def execute():
    frappe.log_error("Starting seat population patch", "populate_seats.py")  # Optional: for debugging

    # Get all tickets where seat is NULL (not set yet)
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": None}, fields=["name"])

    
    for ticket in tickets:
        # Generate seat like 56C, 87A, etc.
        seat = f"{random.randint(1, 99)}{random.choice('ABCDE')}"
        
        # Update the seat field in the DB
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

    # Commit the changes to the database
    frappe.db.commit()

    frappe.log_error(f"Updated {len(tickets)} tickets", "populate_seats.py")  # Optional: to confirm how many were updated
