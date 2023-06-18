#!/usr/bin/python3
"""
Lists all cities with a name starting with 
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    city_name = sys.argv[4]
    query = """
            SELECT * 
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE cities.name LIKE %s
            ORDER BY cities.id ASC;
            """
    cur.execute(query, (city_name + "%",))
    cities = cur.fetchall()
    city_list = []
    for city in cities:
        city_list.append(city[0])
        print(', '.join(city_list))
