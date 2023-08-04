#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv


# Algo de many-to-many hecho
# place_amenity = Table('association', Base.metadata,
#                       Column('place_id', ForeignKey('place.id')),
#                       Column('amenity_id', ForeignKey('amenity.id'))
#                       )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(
        "cities.id"), nullable=False)  # ""
    user_id = Column(String(60), ForeignKey(
        "users.id"), nullable=False)  # ""
    name = Column(String(128), nullable=False)  # ""
    description = Column(String(1024), nullable=True)  # ""
    number_rooms = Column(Integer, default=0, nullable=False)  # 0
    number_bathrooms = Column(Integer, default=0, nullable=False)  # 0
    max_guest = Column(Integer, default=0, nullable=False)  # 0
    price_by_night = Column(Integer, default=0, nullable=False)  # 0
    latitude = Column(Float)  # 0.0
    longitude = Column(Float)  # 0.0
    amenity_ids = []  # No longer in use in db
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", cascade='all, delete, delete-orphan', backref="place")
    else:
        @property
        def reviews(self):
            """"Returns cities that share state.id"""
            from models import storage

            reviewsOfPlace = []
            for object in storage.all():
                if object.__class__.__name__ == 'Review':
                    if object.place_id == self.id:
                        reviewsOfPlace.append(object)
