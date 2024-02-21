#!/usr/bin/python3
"""
Module that prints all city objects
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    rows = session.query(State).join(City).order_by(City.id.asc()).all()

    for row in rows:
        print(f"{row.name}: ({City.id}) {City.name}")

    session.close()
