#!/usr/bin/python3
"""
module to add a new name states databases
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def add_new():
    """
    function to add new name states
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    new_state = session.query(State).filter(State.name == "Louisiana").first()
    print(new_state.id)


if __name__ == "__main__":
    add_new()
