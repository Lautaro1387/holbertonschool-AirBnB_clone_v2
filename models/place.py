#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
import os
user = os.environ.get('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """A place to stay"""
    if user == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review", backref="place",
                cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                backref="places", viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        amenity_ids = []


    @porperty
    def reviews(self):
        """reviews"""
        revlist = []
        for review in storage.all(Review).values():
            if self.id == review.place_id:
                revlist.append(models.storage.all(Review)[review])
        return revlist

    @property
    def amenities(self):
        """amenities"""
        amelist = []
        for amenity in sotrage.all(Amenity).value():
            if self.id == amenity.place_id:
                amelist.append(models.storage.all(Amenity)[amenity])
        return amelist

    @amenities.setter
    def amenities(self, obj):
        """amenities obj"""
        if type(obj).__name__ == "Amenity"
            self.obj.append(obj.id)
