#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import os
strg = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if strg == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                cascade="all, delete")
    else:
        name = ""

    @property
    def cities(self):
        """Getter"""
        from models.city import City
        for obj in models.storage.City.values():
            if obj.state._id == self.id:
                return obj
