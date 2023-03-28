import sqlite3
import os


class ConnexionBdd:
    def __init__(self):
        self.repertoire = os.path.dirname(__file__)
        self.path_bdd = os.path.join(self.repertoire, "users.db")
        self.conn = sqlite3.connect(self.path_bdd)
        self.cursor = self.conn.cursor()
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """
        )
        self.conn.commit()

    def register_user(self, username, password):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password),
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def check_credentials(self, username, password):
        self.cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password),
        )
        return self.cursor.fetchone() is not None
