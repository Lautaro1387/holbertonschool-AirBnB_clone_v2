#!/usr/bin/python3
"""New engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """engine"""
    __engine = None
    __session = None

    __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                "hbnb_dev", ,),
                                pool_pre_ping=True)
