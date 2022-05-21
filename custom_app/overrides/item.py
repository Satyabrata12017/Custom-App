import frappe
import json


@frappe.whitelist()
def update_custom_field(self,method=None):
        if self.variant_of:
                if not self.width:
                        for i in self.attributes:
                                if i.attribute == "Height":
                                        self.height=i.attribute_value
                                if i.attribute == "Width":
                                        self.width=i.attribute_value
                                if i.attribute == "Yield":
                                        self.yeild=i.attribute_value
                                if i.attribute == "Length":
                                        self.length = i.attribute_value
@frappe.whitelist()
def update_uom_table(self,method=None):
	if self.width:
		for i in self.uoms:
			if i.uom == "Kg":
				i.formula=float(self.length)*float(self.width)*1.441
			if i.uom == "Cubic Meter":
				i.formula = float(self.length)*float(self.width)*float(self.height)
