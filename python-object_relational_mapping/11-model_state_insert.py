#!/usr/bin/python3
"""
Create a new state named 'Louisiana'
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

    # Create new State object
    new_state = State(name='Louisiana')

    with Session() as session:
        # Add the new State object to the session
        session.add(new_state)
        session.commit()
        print(new_state.id)
