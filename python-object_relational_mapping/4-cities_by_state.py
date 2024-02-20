#!/usr/bin/python3
"""
Module to work with MySQLdb and python
"""
import sys
import MySQLdb


def list_cities(user_name, password, dbase):
    """List all cities from database

    Args:
        user_name (str): User for localhost
        password (str): user password
        dbase (str): database to use
    """

    db = MySQLdb.connect(host="localhost",
                         user=user_name,
                         passwd=password,
                         port=3306,
                         database=dbase)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON cities.state_id = states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
