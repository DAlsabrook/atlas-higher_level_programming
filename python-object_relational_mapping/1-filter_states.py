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
    cur.execute("SELECT * FROM states;")
    rows = cur.fetchall()
    for row in rows:
        if str(row[1]).startswith("N"):
            print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    name_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
