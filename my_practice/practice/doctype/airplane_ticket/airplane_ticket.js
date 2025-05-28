// Copyright (c) 2025, AKanksha and contributors

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        frm.add_custom_button('Select Seat', () => {
            let d = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: true
                    }
                ],
                primary_action_label: 'Set Seat',
                primary_action(values) {
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });

            d.show();
        });
    },
    flight_no: function (frm) {
    if (frm.doc.flight_no) {
      frappe.model.get_doc('Flight', frm.doc.flight_no)
        .then(flight => {
          frm.set_value('gate_number', flight.gate_number);
        });
    }
  }
});

