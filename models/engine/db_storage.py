#!/usr/bin/python3
"""New engine"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os
user = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')
env = os.environ.get('HBNB_ENV')

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            #objs.extend(self.__session.query(Amenity).all())
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        self.__session.commit()
    
    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
