#!/usr/bin/python3
from MySQLdb import _mysql
import sys


def sql_connect(user, pw, db_name):

    db=_mysql.connect(host="localhost",
                        port=3306,
                        password= pw,
                        database= db_name)
    print("Connected")

print(f"{sys.argv[1]}, {sys.argv[2]}, {sys.argv[3]}")
sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
