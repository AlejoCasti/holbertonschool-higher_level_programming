#!/usr/bin/python3
''' Script that lists all states form database '''
import MySQLdb
import sys

if __name__ == '__main__':

    arg = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=arg[1],
                         password=arg[2], database=arg[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name =\
    @0 ORDER BY id ASC "
    cursor.execute(query, sys.argv[4])
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    db.close()
