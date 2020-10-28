import mysql.connector


class MySQLAPI:
    def __init__(self, host, user, password, database):
        print("\nInitialising API...")

        print(" - Connecting to database...")
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(" - Connected.")

        self.cursor = self.db.cursor()

        print("API initialised.")

    def clear(self, table, condition=None):
        print(f"\nClearing {table}...")

        self.cursor.execute(f"DELETE FROM {table}")
        if condition is not None:
            self.cursor.execute(f"WHERE {condition}")

        print(f"{table} has been cleared.")

    def list_to_db(self, table, val):
        print(f"\nInserting list into {table}...")

        # Inserts everything in the given list into the table given using the execute many command
        sql = f"INSERT INTO {table} (firstname, lastname, age) VALUES (%s, %s, %s)"
        self.cursor.executemany(sql, val)

        self.db.commit()

        print(f"{len(val)} records inserted | Last ID: {self.cursor.lastrowid}")

    def db_to_list(self, table):
        print(f"\nInserting {table} into list...")

        self.cursor.execute(f"SELECT * FROM {table}")

        print(f"{len(self.cursor.fetchall())} records collected.")
        return [x for x in self.cursor.fetchall()]

