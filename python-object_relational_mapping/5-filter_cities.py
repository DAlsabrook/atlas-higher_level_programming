#!/usr/bin/python3
"""
Module to use sql and python
"""
import sys
import MySQLdb


def list_cities_of_state(user_name, password, dbase, state_name):
    """List all cities of a state

    Args:
    user_name (str): User for localhost
    password (str): user password
    dbase (str): database to use
    """
    db = MySQLdb.connect(host="localhost",
                         user=user_name,
                         passwd=password,
                         database=dbase,
                         port=3306)
    cur = db.cursor()
    query = "SELECT cities.name\
                FROM cities INNER JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY states.name ASC;"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    cities_str = ', '.join(cities)
    print(cities_str)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities_of_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
