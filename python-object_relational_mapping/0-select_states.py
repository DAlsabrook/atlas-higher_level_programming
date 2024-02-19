#!/usr/bin/python3
"""
This is a module to import a database and work with it
"""
from MySQLdb import _mysql
import sys


def sql_connect(user, pw, db_name):
    """
    This is a method to import a database
    """

    print("Inside method")
    db=_mysql.connect(host="localhost",
                        port=3306,
                        password= pw,
                        database= db_name)
    print(f"db = {db}")

if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
