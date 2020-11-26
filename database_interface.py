import sqlite3
from sqlite3 import Error

class DatabaseInterface:
    def __init__(self, db_name):
        self.conn = None
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            ) """)
    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur
    
    def register_new_user(self, loginEntr, passwordEntr, messagebox):
        username = loginEntr.get()
        password = passwordEntr.get()
        self.cur.execute("SELECT username FROM Users WHERE username = ?", (username,))
        is_user = self.cur.fetchone()
        if not is_user:
            self.execute("INSERT INTO Users (username, password) VALUES (?, ?) ", (username, password))
            messagebox.showinfo("Success!", "Registered!")
        else:
            messagebox.showinfo("Register failed", "There is a user with the same login")

    def login_user(self, login_entry, password_entry, messagebox, parent):
        user = login_entry.get()
        password = password_entry.get()
        self.cur.execute("SELECT username FROM Users WHERE username = ?", (user,))
        is_username_in_db = self.cur.fetchone()
        self.cur.execute("SELECT password FROM Users WHERE password = ?", (password,))
        usernames_password = self.cur.fetchone()
        if is_username_in_db and usernames_password:
            parent.withdraw()
            parent.master.deiconify()
        else:
            messagebox.showinfo("Login Invalid", "Invalid Login")

    def __del__(self):
        self.conn.close()


'''if __name__ == "__main__":
    db = DatabaseInterface("to-do.db")
    db.register_new_user('piotr', 'kawicz')
    db.register_new_user('admin', 'admin')'''

