#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'place.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


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
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False, back_populates="places_amenities")
    else:
        @property
        def reviews(self):
            from models import storage
            reviews = []
            for key, value in storage.__objects.items():
                splited_key = key.split('.')
                if splited_key[0] == 'Review':
                    reviews.append(value)
            filtered_reviews = list(
                filter(lambda x: x.place_id == self.id), reviews)
            return filtered_reviews

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == 'Amenity' and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
