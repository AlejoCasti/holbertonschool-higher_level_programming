#!/usr/bin/python3
''' Script that lists all states form database '''
import MySQLdb
import sys

if __name__ == '__main__':

    arg = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=arg[1],
                         password=arg[2], database=arg[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY\
    id ASC".format(sys.argv[4])
    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    db.close()
