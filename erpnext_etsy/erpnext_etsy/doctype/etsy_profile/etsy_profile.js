// Copyright (c) 2017, Jonathan Martin and contributors
// For license information, please see license.txt

frappe.ui.form.on('Etsy Profile', {
	refresh: function(frm) {
		console.log("Refreshing")
		if (frm.doc.enable_sync === 1) {
			console.log("Adding Sync Etsy button")
			frm.add_custom_button(__('Sync Etsy'), function() {
				console.log("Calling erpnext_etsy.api.sync_etsy")
				frappe.call({
					"method" : "erpnext_etsy.api.sync_etsy", 
					"args" : {
						"etsy_shop_name" : frm.doc.etsy_shop_name
					} 
				})
			}).addClass("btn-primary");
		}
	}
});
