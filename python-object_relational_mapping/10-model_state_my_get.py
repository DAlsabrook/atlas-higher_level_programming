#!/usr/bin/python3
"""
module to search database for a specific name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbase}'
        )
    Base.metadata.bind = engine
    DBsession = sessionmaker(bind=engine)
    session = DBsession()

    rows=session.query(State).filter(State.name.ilike(f'%{state_name}%')).all()

    for row in rows:
        print(f"{row.id}: {row.name}")

    session.close()
