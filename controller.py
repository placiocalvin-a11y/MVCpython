# controller.py
import tkinter as tk
from tkinter import messagebox
import re

EMAIL_RE = re.compile(r"[^@]+@[^@]+\.[^@]+")

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.selected_id = None

        # Bind buttons
        self.view.add_btn.config(command=self.add_user)
        self.view.update_btn.config(command=self.update_user)
        self.view.delete_btn.config(command=self.delete_user)
        self.view.load_btn.config(command=self.refresh_table)

        # Bind table selection
        self.view.table.bind("<<TreeviewSelect>>", self.on_row_select)

    def validate(self, name, email, age):
        if not name.strip() or not email.strip():
            return False, "Name and Email are required."
        if not EMAIL_RE.match(email):
            return False, "Invalid email format."
        if age.strip() and not age.isdigit():
            return False, "Age must be numeric."
        return True, ""

    def add_user(self):
        name = self.view.name_var.get()
        email = self.view.email_var.get()
        age = self.view.age_var.get()
        ok, msg = self.validate(name, email, age)
        if not ok:
            self._alert(msg); return
        try:
            self.model.add_user(name, email, int(age) if age else None)
            self.refresh_table()
            self._clear_form()
        except Exception as e:
            self._alert(str(e))

    def refresh_table(self):
        for r in self.view.table.get_children():
            self.view.table.delete(r)
        for row in self.model.get_all_users():
            self.view.table.insert("", tk.END, values=row)

    def on_row_select(self, event):
        sel = self.view.table.selection()
        if sel:
            vals = self.view.table.item(sel[0])["values"]
            self.selected_id = vals[0]
            self.view.name_var.set(vals[1])
            self.view.email_var.set(vals[2])
            self.view.age_var.set(vals[3] if vals[3] is not None else "")

    def update_user(self):
        if not self.selected_id:
            self._alert("Select a row to update."); return

        if messagebox.askyesno("Confirm", "Are you sure you want to update selected user?"):
            try:
                name = self.view.name_var.get();
                email = self.view.email_var.get();
                age = self.view.age_var.get()
                ok, msg = self.validate(name, email, age)
                if not ok:
                    self._alert(msg);
                    return
                self.model.update_user(self.selected_id, name, email, int(age) if age else None)
                self.refresh_table()
                self._clear_form()
            finally:
                pass

    def delete_user(self):
        if not self.selected_id:
            self._alert("Select a row to delete."); return
        if messagebox.askyesno("Confirm", "Delete selected user?"):
            try:
                self.model.delete_user(self.selected_id)
                self.refresh_table()
                self.model.delete_user(self.selected_id)
                self.refresh_table()
                self._clear_form()
            finally:
                pass
    def _clear_form(self):
        self.view.name_var.set(""); self.view.email_var.set(""); self.view.age_var.set("")
        self.selected_id = None

    def _alert(self, message):
        from tkinter import messagebox
        messagebox.showinfo("Info", message)
