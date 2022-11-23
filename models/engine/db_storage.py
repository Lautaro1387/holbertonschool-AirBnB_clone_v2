#!/usr/bin/python3
"""New engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import os.environ.get('HBNB_MYSQL_USER') as user
import os.environ.get('HBNB_MYSQL_PWD') as pwd
import os.environ.get('HBNB_MYSQL_HOST') as host
import os.environ.get('HBNB_MYSQL_DB') as db

class DBStorage:
    """engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                user, pwd, host)
                                pool_pre_ping=True)
