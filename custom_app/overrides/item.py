import frappe
import json


@frappe.whitelist()
def update_custom_field(self,method=None):
        frappe.msgprint("Satya")
        if self.variant_of:
                for i in self.attributes:
                        if i.attribute == "Height":
                                self.height=i.attribute_value
                        if i.attribute == "Width":
                                self.width=i.attribute_value
                        if i.attribute == "Yield":
                                self.yield=i.attribute_value
