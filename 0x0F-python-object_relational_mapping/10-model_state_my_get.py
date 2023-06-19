#!/usr/bin/python3
"""
query 'name' containing from states databases
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def list_having_name_from_states():
    """
    list states with name passed
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])

    name = sys.argv[4]
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name)\
        .order_by(State.id).first():
            if state is not None:
                print(state.id)
            else:
                print("Not found")


if __name__ == "__main__":
    list_having_name_from_states()
