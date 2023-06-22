#!/usr/bin/python3

"""
The model city module

define the first city model
a python file that contains the class definition of a
State and an instance Base = declarative_base():

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys


class City(Base):
    """"
    inherits from Base Tips
    id: that represents a column of an auto-generated,unique integer,
    can’t be null and is a primary key
    name: that represents a column of a string with maximum 128 characters
    and can’t be null
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
