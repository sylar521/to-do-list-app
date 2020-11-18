from login import Login
from interface import Interface
import tkinter as tk
from tkinter import messagebox

class MainApp():
    def __init__(self):
        root = tk.Tk()
        Login(root)
        interface = Interface(root)
        interface.master.title("To-Do-List")
        interface.mainloop()
        #if Login.onButtonPress(self):
            #messagebox.showinfo("Login", "Login")

if __name__=='__main__':
    MainApp()