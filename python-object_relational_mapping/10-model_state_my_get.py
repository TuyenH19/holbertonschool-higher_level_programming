#!/usr/bin/python3
"""
Print the State object with the name passed as argument from the database
"""
import sys

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, database), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    with Session() as session:
        found_state = session.query(
            State).filter(State.name == state_name).first()
        print_text = found_state.id \
            if found_state else "Not found"
        print(print_text)
