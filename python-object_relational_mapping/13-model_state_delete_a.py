#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a
"""
import sys

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.query(State).filter(State.name.like('%a%')).delete()
        session.commit()
