#!/usr/bin/python3
"""
query all the cities
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
import sys


def list_cities():
    """
    list all cities
    """
    user = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(user, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        for city in state.cities:
            print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    list_cities()
