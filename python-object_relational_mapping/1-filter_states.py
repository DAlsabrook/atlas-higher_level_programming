#!/usr/bin/python3
"""
This module is for running a MySQLdb method
"""
import sys
import MySQLdb


def name_with_n(user_name, password, dbase):
    """This method finds all names that start with a "N"

    Args:
        user_name (str): localhost user
        password (str): user password
        dbase (str): database to use
    """
    db = MySQLdb.connect(host = "localhost",
                         user = user_name,
                         passwd = password,
                         database = dbase,
                         port = 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row[2])
        if str(row[2]).startswith("N"):
            print(row)
    cur.close()
    db.close()
