frappe.ready(function () {
    // Wait for DOM to load
    const website = frappe.web_form.get_value('website');

    if (website) {
        const link = document.createElement('a');
        link.href = website;
        link.textContent = "Visit Official Website";
        link.target = "_blank";
        link.style = "display: block; margin-top: 15px; color: #007bff; text-decoration: underline;";

        // Append after the Website field
        const websiteField = document.querySelector('[data-fieldname="website"]');
        if (websiteField) {
            websiteField.parentNode.appendChild(link);
        }
    }
});
