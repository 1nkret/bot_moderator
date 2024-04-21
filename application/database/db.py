from application.database.db_connection import DbConnection


def create_table():
    with DbConnection() as con:
        return con.execute(f"""CREATE TABLE IF NOT EXISTS punishments
        (id INTEGER PRIMARY KEY AUTOINCREMENT ,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        from_user_id INTEGER,
        message TEXT,
        date DATETIME
        )""")


if __name__ == "__main__":
    create_table()
