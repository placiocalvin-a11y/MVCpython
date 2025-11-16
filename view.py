# view.py
import tkinter as tk
from tkinter import ttk

class UserView:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management")

        # Variables
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()

        # Form
        tk.Label(root, text="Name").grid(row=0, column=0, sticky="w")
        tk.Entry(root, textvariable=self.name_var).grid(row=0, column=1, padx=5)

        tk.Label(root, text="Email").grid(row=1, column=0, sticky="w")
        tk.Entry(root, textvariable=self.email_var).grid(row=1, column=1, padx=5)

        tk.Label(root, text="Age").grid(row=2, column=0, sticky="w")
        tk.Entry(root, textvariable=self.age_var).grid(row=2, column=1, padx=5)

        # Buttons
        self.add_btn = tk.Button(root, text="Add")
        self.add_btn.grid(row=3, column=0, pady=6)
        self.update_btn = tk.Button(root, text="Update")
        self.update_btn.grid(row=3, column=1)
        self.delete_btn = tk.Button(root, text="Delete")
        self.delete_btn.grid(row=4, column=0)
        self.load_btn = tk.Button(root, text="Load")
        self.load_btn.grid(row=4, column=1)

        # Table
        cols = ("id", "name", "email", "age")
        self.table = ttk.Treeview(root, columns=cols, show="headings", height=8)
        for c in cols:
            self.table.heading(c, text=c.upper())
            self.table.column(c, width=100)
        self.table.grid(row=5, column=0, columnspan=2, pady=10)
