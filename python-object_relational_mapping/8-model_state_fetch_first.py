#!/usr/bin/python3
"""
Module t get the first state from "states" table
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbase}'
        )
    Base.metadata.bind = engine
    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    row = session.query(State).order_by(State.id.asc()).first()
    if row is not None:
        print(f"{row.id}: {row.name}")
    else:
        print("Nothing")

    session.close()
