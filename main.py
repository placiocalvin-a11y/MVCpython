# main.py
import tkinter as tk
from database import get_connection
from model import UserModel
from view import UserView
from controller import UserController

def main():
    root = tk.Tk()
    conn = get_connection("app.db")    # SQLite
    model = UserModel(conn)
    view = UserView(root)
    controller = UserController(model, view)
    controller.refresh_table()
    root.mainloop()

if __name__ == "__main__":
    main()
