#!/usr/bin/python3
"""
Lists all states with a name starting with N
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    state_name = sys.argv[4]
    query = ("SELECT * FROM states \
            WHERE name = %s ORDER BY id ASC;")
    cur.execute(query, (state_name),)
    states = cur.fetchall()

    for state in states:
        if (state[1] == state_name):
            print(state)
