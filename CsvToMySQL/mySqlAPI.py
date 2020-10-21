import mysql.connector


class MySQLAPI:
    def __init__(self, database, secret):
        print("\nInitialising API...")
        self.database_name = database
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password=secret,
            database=database
        )
        self.cursor = self.db.cursor()
        print("API initialised.")

    def list_to_db(self, table, val):
        print("\nInserting list into", self.database_name, ":", table)
        sql = f"INSERT INTO {table} (firstname, lastname, age) VALUES (%s, %s, %s)"

        self.cursor.executemany(sql, val)

        self.db.commit()
        print(len(val), "records inserted | Last ID:", self.cursor.lastrowid)

    def db_to_list(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")

        return [x for x in self.cursor.fetchall()]

