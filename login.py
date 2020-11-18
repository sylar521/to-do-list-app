class Login():
    def login(self, login_entry, password_entry, messagebox):
        self.user = login_entry.get()
        self.password = password_entry.get()
        if self.user == 'Piotr' and self.password == "Kawicz":
            self.withdraw()
            self.master.deiconify()
        else:
            messagebox.showinfo("Login Invalid", "Invalid Login")