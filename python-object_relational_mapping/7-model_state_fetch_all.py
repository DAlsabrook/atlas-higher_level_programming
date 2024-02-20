#!/usr/bin/python3
"""List all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Assuming model_state.py is correctly set up


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbase}')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    rows = session.query(State).order_by(State.id.asc()).all()

    for row in rows:
        print(f"{row.id}: {row.name}")

    session.close()
