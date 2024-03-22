#!/usr/bin/python3
"""Update state name id 2 to 'New Mexico'
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
        found_state = session.query(
            State).filter_by(id=2).first()
        found_state.name = "New Mexico"
        session.commit()
