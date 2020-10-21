secret = 'Jovili04'

from csv_file_reader import get_list_with_tuples
from mySqlAPI import MySQLAPI


def main():
    val = get_list_with_tuples('main.csv')

    mySqlAPI = MySQLAPI('namedatabase', secret)

    mySqlAPI.list_to_db('persons', val)

    print(mySqlAPI.db_to_list('persons'))


if __name__ == '__main__':
    main()
