#!/usr/bin/python3
"""
query first state
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def first_state():
    """
    list the first state
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if (first_state == None):
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))



if __name__ == "__main__":
    first_state()
