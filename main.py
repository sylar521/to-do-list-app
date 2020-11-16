from login import Login
from interface import Interface

class MainApp():
    def __init__(self):
        loginWindow = Login()
        loginWindow.master.title("Login")
        loginWindow.mainloop()
        login = loginWindow.LoginEntry.get()
        password = loginWindow.PasswordEntry.get()
        if login == "Piotr" and password == "Kawicz":
            loginWindow.destroy()
            interface = Interface()
            interface.master.title("To-Do-List")
            interface.mainloop()

if __name__=='__main__':
    MainApp()