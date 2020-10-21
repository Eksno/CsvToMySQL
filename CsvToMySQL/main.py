secret = 'Jovili04'

from csvToList import get_list
from mySqlAPI import MySQLAPI


def main():
    val = get_list('main.csv')

    mySqlAPI = MySQLAPI('namedatabase', secret)

    mySqlAPI.list_to_db('persons', val)

    print(mySqlAPI.db_to_list('persons'))


if __name__ == '__main__':
    main()
