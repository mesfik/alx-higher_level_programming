#!/usr/bin/python3
"""
module to update a new name states databases
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


def update_new():
    """
    function to update new name states
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    update = session.query(State).filter(State.id==2).first()

    if update:
        update.name = "New Mexico"

        session.commit()


if __name__ == "__main__":
    update_new()
