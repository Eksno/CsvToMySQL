from csvReader import csvToList
from mySqlAPI import MySQLAPI


def main():
    val = csvToList('main.csv')

    host = input("host")
    user = input("user")
    password = input("password: ")
    database = input("database: ")
    table = input("table: ")

    mySqlAPI = MySQLAPI(host, user, password, database)

    mySqlAPI.list_to_db(table, val)

    print(mySqlAPI.db_to_list(table))


if __name__ == '__main__':
    main()
