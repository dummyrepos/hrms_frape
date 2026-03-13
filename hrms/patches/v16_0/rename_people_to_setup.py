import frappe


def execute():
	for doctype in ("Workspace Sidebar", "Workspace", "Desktop Icon"):
		if frappe.db.exists(doctype, "People"):
			frappe.delete_doc(doctype, "People", force=True, ignore_permissions=True)

	frappe.clear_cache()
