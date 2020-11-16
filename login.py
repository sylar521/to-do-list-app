import tkinter as tk

class Login(tk.Frame):
    def createLabels(self):
        self.LoginLabel = tk.Label(self, text="Login")
        self.LoginLabel.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.PasswordLabel = tk.Label(self, text="Password")
        self.PasswordLabel.grid(row = 1, column = 0, padx = 10, pady = 10)

    def createEntries(self):
        self.LoginEntry = tk.Entry(self)
        self.LoginEntry.grid(row = 0, column = 1)
        self.PasswordEntry = tk.Entry(self, show = "*")
        self.PasswordEntry.grid(row = 1, column = 1)
    
    def createButtons(self):
        self.LoginButton = tk.Button(self, text = "Login")
        self.LoginButton.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.ExitButton = tk.Button(self, text = "Exit", command = self.master.destroy)
        self.ExitButton.grid(row = 2, column = 1, padx = 10, pady = 10)

    def createLoginWindow(self):
        self.createLabels()
        self.createEntries()
        self.createButtons()


    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createLoginWindow()
