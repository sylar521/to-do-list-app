from login_window import LoginWindow
from interface import Interface
import tkinter as tk
from tkinter import messagebox
from database_interface import DatabaseInterface

class MainApp():
    def __init__(self):
        root = tk.Tk()
        LoginWindow(root)
        interface = Interface(root)
        interface.master.title("To-Do-List")
        interface.mainloop()

if __name__=='__main__':
    MainApp()