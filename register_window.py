import tkinter as tk
#from tkinter import messagebox
#from login import Login

class RegisterWindow(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.master = master
        self.grid()
        self.resizable(width = False, height = False)
        self.title("Register")
        self.createTopLevel()
        self.grab_set()

    def createTopLevel(self):
        self.TopLevelLabels()
        self.TopLevelEntries()
        self.TopLevelButtons()

    def TopLevelLabels(self):
        self.NewUserLoginLabel = tk.Label(self, text="Login")
        self.NewUserLoginLabel.grid(row = 0, column = 0, sticky = "W")
        self.NewUserPasswordLabel = tk.Label(self, text="Password")
        self.NewUserPasswordLabel.grid(row = 1, column = 0, sticky = "W")

    def TopLevelEntries(self):
        self.NewUserLoginEntry = tk.Entry(self)
        self.NewUserLoginEntry.grid(row = 0, column = 1)
        self.NewUserPasswordEntry = tk.Entry(self, show = "*")
        self.NewUserPasswordEntry.grid(row = 1, column = 1)
    
    def TopLevelButtons(self):
        self.RegisterButton = tk.Button(self, text = "Register")
        self.RegisterButton.grid(row = 2, column = 0, sticky = "W")
        self.ExitButton = tk.Button(self, text = "Cancel", command = self.destroy)
        self.ExitButton.grid(row = 2, column = 3)
