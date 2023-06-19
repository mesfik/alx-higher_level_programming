#!/usr/bin/python3
"""
query 'a' containing from states databases
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def list_having_a_from_states():
    """
    list all states
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    list_having_a_from_states()
