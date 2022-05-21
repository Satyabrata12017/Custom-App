frappe.provide("erpnext.item");

frappe.ui.form.on("Item", {
	validate: function(frm) {
		msgprint("Satya Test");
		if (frm.width != 0 || frm.length != 0){
			uom_data=frm.uoms;
			uom_data.forEach((item, index) => {
				console.log(`${index} : ${item}`);
			});

		}

	}

});
