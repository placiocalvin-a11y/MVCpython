# model.py
class UserModel:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_user(self, name, email, age):
        query = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
        self.cursor.execute(query, (name, email, age))
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT id, name, email, age FROM users")
        return self.cursor.fetchall()

    def update_user(self, user_id, name, email, age):
        query = "UPDATE users SET name=?, email=?, age=? WHERE id=?"
        self.cursor.execute(query, (name, email, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.conn.commit()
