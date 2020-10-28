from csvReader import csv_to_list
from mySqlAPI import MySQLAPI


def main():
    val = csv_to_list('people.csv')

    host, user, password, database, table = get_login_details()

    my_sql_api = MySQLAPI(host, user, password, database)

    my_sql_api.clear(table)

    my_sql_api.list_to_db(table, val)

    val = my_sql_api.db_to_list(table)

    print("\n\n\nAnswers:")
    print("rowcount:", my_sql_api.rowcount(table))
    print("The lastnames of all people named \"Blake\":", [p[2] for p in val if p[1] == "Blake"])
    print("Youngest people:", [p for p in val if p[3] == min([p[3] for p in val])])
    print("Oldest people:", [p for p in val if p[3] == max([p[3] for p in val])])
    print("Age Difference between youngest and oldest:", max([p[3] for p in val]) - min([p[3] for p in val]))
    print("Average age:", sum([p[3] for p in val]) / len([p[3] for p in val]))
    print("")


def get_login_details():
    try:
        login_details = csv_to_list('databases.csv')[1]
        host = login_details[0]
        user = login_details[1]
        password = login_details[2]
        database = login_details[3]
        table = login_details[4]
    except FileNotFoundError:
        host = input("host: ")
        user = input("user: ")
        password = input("password: ")
        database = input("database: ")
        table = input("table: ")
    return host, user, password, database, table


if __name__ == '__main__':
    main()
