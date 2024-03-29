#!/usr/bin/python3
"""
Module to delete all objects containing the letter a
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

    rows = session.query(State).filter(State.name.ilike("%a%"))
    for row in rows:
        session.delete(row)
    session.commit()
    session.close()
