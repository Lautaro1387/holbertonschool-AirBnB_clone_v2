#!/usr/bin/python3
"""New engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import os.environ.get('HBNB_MYSQL_USER')
import os.environ.get('HBNB_MYSQL_PWD')
import os.environ.get('HBNB_MYSQL_HOST')
import os.environ.get('HBNB_MYSQL_DB')

class DBStorage:
    """engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                "hbnb_dev", ,)
                                pool_pre_ping=True)
