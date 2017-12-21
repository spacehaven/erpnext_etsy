from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Integrations"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Etsy Profiles",
					"description": _("ERPNext Etsy Connector Profiles"),
					"hide_count": True
				}
			]
		}
	]
