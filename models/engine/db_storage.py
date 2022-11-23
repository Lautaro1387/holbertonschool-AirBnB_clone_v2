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
        if HBNB_ENV == 'test':
            #Base.metadata.drop_all

    def all(self, cls=None):
        self.__session.query(cls)
        if cls == None:
            #for k in FileStorage.__objects.id:

    def new(self, obj):
        self.__session.add()

    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(engine)
        