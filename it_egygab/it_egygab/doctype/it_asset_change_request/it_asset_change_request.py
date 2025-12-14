# Copyright (c) 2025, Mahmoud and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ITAssetChangeRequest(Document):

	def on_submit(self):
		#self.current_cheque_status="Issued"
		#self.save()
		#frappe.db.commit()
		_it_asset = frappe.get_doc('IT Assets', self.asset)
		_it_asset.it_user=self.asset_user
		_it_asset.location=self.location
		_it_asset.status=self.asset_status
		#print (self.location)
		_it_asset.save()
		frappe.db.commit()

