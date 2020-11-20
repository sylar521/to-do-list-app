import tkinter as tk
from tkinter import messagebox
from login import Login
from register_window import RegisterWindow

class LoginWindow(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.grid()
        self.resizable(width = False, height = False)
        self.protocol("WM_DELETE_WINDOW", self.master.destroy)
        self.title("Login")
        self.createTopLevel()

    def createTopLevel(self):
        self.TopLevelLabels()
        self.TopLevelEntries()
        self.TopLevelButtons()
        self.master.withdraw()

    def TopLevelLabels(self):
        self.LoginLabel = tk.Label(self, text="Login")
        self.LoginLabel.grid(row = 0, column = 0, sticky = "W")
        self.PasswordLabel = tk.Label(self, text="Password")
        self.PasswordLabel.grid(row = 1, column = 0, sticky = "W")

    def TopLevelEntries(self):
        self.LoginEntry = tk.Entry(self)
        self.LoginEntry.grid(row = 0, column = 1)
        self.PasswordEntry = tk.Entry(self, show = "*")
        self.PasswordEntry.grid(row = 1, column = 1)
    
    def TopLevelButtons(self):
        self.LoginButton = tk.Button(self, text = "Login", command = \
            lambda:[Login.login(self, login_entry=self.LoginEntry, password_entry=self.PasswordEntry, messagebox=messagebox)])
        self.LoginButton.grid(row = 2, column = 2)
        self.ExitButton = tk.Button(self, text = "Exit", command = self.master.destroy)
        self.ExitButton.grid(row = 2, column = 3)
        self.RegisterButton = tk.Button(self, text = "Register", command = lambda:[RegisterWindow(self)])
        self.RegisterButton.grid(row = 2, column = 0, columnspan = 2, sticky = "W")
