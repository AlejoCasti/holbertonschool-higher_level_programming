#!/usr/bin/python3
''' Script that lists all states form database '''
import MySQLdb
import sys

if __name__ == '__main__':

    arg = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=arg[1],
                         password=arg[2], database=arg[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities \
    WHERE cities.state_id = \
    (SELECT id FROM states WHERE name = %(name)s) \
    ORDER BY id ASC", {'name': sys.argv[4]})
    records = cursor.fetchall()

    i = ''
    for city in query_row:
        print(i + str(*city), end='')
        i = ', '

    print('')
    cursor.close()
    db.close()
