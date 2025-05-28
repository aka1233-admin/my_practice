// Copyright (c) 2025, AKanksha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function (frm) {
        // Check if the website field is filled
        if (frm.doc.website) {
            // Add a custom button to the form
            frm.add_custom_button('Visit Website', () => {
                // Open the website in a new tab
                window.open(frm.doc.website, '_blank');
            }, __('Actions'));
        }
    }
});

