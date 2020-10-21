from csvReader import csvToList
from mySqlAPI import MySQLAPI


def main():
    val = csvToList('main.csv')

    mySqlAPI = MySQLAPI('namedatabase', 'password_to_db')

    mySqlAPI.list_to_db('persons', val)

    print(mySqlAPI.db_to_list('persons'))


if __name__ == '__main__':
    main()
