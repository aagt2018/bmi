import sqlite3 as db


class User:
    DATABASE_NAME = 'database.db'
    INSERT_USER_SQL = 'INSERT INTO users (username, password) VALUES (?, ?)'
    SELECT_USER_SQL = 'SELECT username, password FROM users WHERE username=?'
    DELETE_USER_SQL = 'DELETE FROM users WHERE username=?'

    def __init__(self):
        pass

    def add(self, user, password):
        existing_user = self.get(user)
        if existing_user:
            return existing_user[0][1] == password

        con = db.connect(self.DATABASE_NAME)
        cur = con.cursor()
        cur.execute(self.INSERT_USER_SQL, (user, password))
        con.commit()
        con.close()

        return True

    def get(self, user):
        con = db.connect(self.DATABASE_NAME)
        cur = con.cursor()
        cur.execute(self.SELECT_USER_SQL, (user,))
        users = cur.fetchall()
        con.close()

        return users

    def delete(self, user):
        con = db.connect(self.DATABASE_NAME)
        cur = con.cursor()
        cur.execute(self.DELETE_USER_SQL, (user,))
        con.commit()
        con.close()