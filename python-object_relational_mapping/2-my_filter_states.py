#!/usr/bin/python3
"""
Module to work with MySQLdb and python
"""
import sys
import MySQLdb


def find_state(username, password, dbase, searched):
    """Method to find a state in the database

    Args:
        username (str): Username for database
        password (str): user password
        dbase (str): database to use
        searched (str): State to search database for
    """

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         database=dbase)
    cur = db.cursor()
    table_name = "states"
    cur.execute("SELECT * FROM {0} ORDER BY {0}.id ASC;".format(table_name))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == searched:
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    find_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
