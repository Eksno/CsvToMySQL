from csvReader import csv_to_list
from mySqlAPI import MySQLAPI


def main():
    val = csv_to_list('people.csv')

    host = input("host")
    user = input("user")
    password = input("password: ")
    database = input("database: ")
    table = input("table: ")

    my_sql_api = MySQLAPI(host, user, password, database)

    my_sql_api.list_to_db(table, val)

    print(my_sql_api.db_to_list(table))


if __name__ == '__main__':
    main()
