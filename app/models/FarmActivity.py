import sqlite3
from functools import reduce

class FarmActivity:
    def __init__(self, id, land_id, activity_type, date, description, attachment):
        self.id = id
        self.land_id = land_id
        self.activity_type = activity_type
        self.date = date
        self.description = description
        self.attachment = attachment

    @staticmethod
    def _connect_to_database():
        return sqlite3.connect('your_database.db')

    def save(self):
        # Fungsi lambda untuk menyimpan data aktivitas ke database
        save_to_database = lambda conn: conn.execute(
            "INSERT INTO farm_activity (land_id, activity_type, date, description, attachment) VALUES (?, ?, ?, ?, ?)",
            (self.land_id, self.activity_type, self.date, self.description, self.attachment)
        )
        conn = self._connect_to_database()
        conn.execute("BEGIN")
        save_to_database(conn)
        conn.commit()
        conn.close()

    def update(self):
        # Fungsi lambda untuk memperbarui data aktivitas dalam database
        update_in_database = lambda conn: conn.execute(
            "UPDATE farm_activity SET land_id = ?, activity_type = ?, date = ?, description = ?, attachment = ? WHERE id = ?",
            (self.land_id, self.activity_type, self.date, self.description, self.attachment, self.id)
        )
        conn = self._connect_to_database()
        conn.execute("BEGIN")
        update_in_database(conn)
        conn.commit()
        conn.close()

    @classmethod
    def get_by_id(cls, activity_id):
        # Fungsi lambda untuk mendapatkan aktivitas berdasarkan ID
        get_activity = lambda conn: conn.execute(
            "SELECT * FROM farm_activity WHERE id = ?",
            (activity_id,)
        ).fetchone()

        conn = cls._connect_to_database()
        activity_data = get_activity(conn)
        conn.close()
        return cls(*activity_data) if activity_data else None

    def delete(self):
        # Fungsi lambda untuk menghapus aktivitas berdasarkan ID
        delete_activity = lambda conn: conn.execute(
            "DELETE FROM farm_activity WHERE id = ?",
            (self.id,)
        )

        conn = self._connect_to_database()
        conn.execute("BEGIN")
        delete_activity(conn)
        conn.commit()
        conn.close()
