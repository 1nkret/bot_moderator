from sqlite3 import connect, register_adapter
from datetime import datetime, timedelta


register_adapter(datetime, datetime.isoformat)


class DbConnection:
    """
    Class to connect to db
    """

    def __enter__(self):
        self.con = connect("database.db")
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()


class Database:
    """Class that control database"""

    def __init__(self):
        self.connection = DbConnection()

    def create_table(self) -> None:
        """
        Create table warns if not exist
        :return:
        """
        with self.connection as con:
            con.execute("""CREATE TABLE IF NOT EXISTS warnings
            (id INTEGER PRIMARY KEY AUTOINCREMENT ,
            username TEXT,
            first_name TEXT,
            from_user_id INTEGER,
            reason TEXT,
            message TEXT,
            date DATETIME
            )""")

    def add_note(
        self,
        username: str,
        first_name: str,
        from_user_id: int,
        reason: str,
        message: str,
    ) -> None:
        with self.connection as con:
            con.execute(
                """
            INSERT INTO warnings (username, first_name, from_user_id, reason, message, date)

            VALUES (?, ?, ?, ?, ?, ?)
            """,
                (username, first_name, from_user_id, reason, message, datetime.now()),
            )

    def response_to_check_warns(self, from_user_id: int) -> int:
        with self.connection as con:
            return con.execute(
                """
            SELECT COUNT(*)
            FROM warnings
            WHERE from_user_id=? AND date>?""",
                (from_user_id, datetime.now() - timedelta(days=3)),
            ).fetchone()[0]


db = Database()

if __name__ == "__main__":
    db = Database()
    db.create_table()
    db.add_note("nameeee", "myname", 123, "rofl", "hello world")
    print(db.response_to_check_warns(123))
