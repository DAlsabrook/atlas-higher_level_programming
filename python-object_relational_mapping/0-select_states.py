#!/usr/bin/python3
from MySQLdb import _mysql
import sys
"""This is a module to import a database and work with it
"""


def sql_connect(user, pw, db_name):
    """This is a method to import a database"""

    db=_mysql.connect(host="localhost",
                        port=3306,
                        password= pw,
                        database= db_name)
    print("Connected")

sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
