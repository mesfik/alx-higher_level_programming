#!/usr/bin/python3
"""
module to delete a new name that have "a" states databases
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def delete_a():
    """
    function to delete new name states that have a
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_a = session.query(State).filter(State.name.like("%a%")).all()

    if delete_a:
        session.delete(delete_a)

        session.commit()


if __name__ == "__main__":
    delete_a()
