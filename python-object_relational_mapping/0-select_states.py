#!/usr/bin/python3
"""
This is a module to import a database and work with it
"""
import MySQLdb
import sys


def sql_connect(usr, pw, db_name):
    """
    This is a method to import a database
    """

    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         port=3306,
                         passwd=pw,
                         database=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
