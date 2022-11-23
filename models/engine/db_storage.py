#!/usr/bin/python3
"""New engine"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
user = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
env = os.environ.get('HBNB_ENV')
class DBStorage:
    """engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{host}', pool_pre_ping=True)
