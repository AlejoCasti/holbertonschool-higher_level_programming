#!/usr/bin/python3
''' Script that lists all states form database '''
import MySQLdb
import sys

if __name__ == '__main__':

    arg = sys.argv
    db = MySQLdb.connect(host='localhost', port=3306, user=arg[1],
                         password=arg[2], database=arg[3])
    cursor = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC")
    records = cursor.fetchall()
    for row in records:
        print(row)
    cursor.close()
    db.close()
