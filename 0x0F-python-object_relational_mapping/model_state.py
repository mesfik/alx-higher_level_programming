#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column
import sys
"""
python file that contains the class definition
of a State and an instance
Base = declarative_base()
"""
Base = declarative_base()


class State(Base):
    """
    a state class that inherited from base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
