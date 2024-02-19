#!/usr/bin/python3
"""
This is a module to import a database and work with it
"""
import MySQLdb
import sys


def sql_connect(user, pw, db_name):
    """
    This is a method to import a database
    """

    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        passwd= pw,
                        database= db_name)
    cur = db.cursor()
    cur.execute("USE hbtn_0e_0_usa SELECT id, name FROM states")

if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
