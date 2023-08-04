#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(
        "cities.id"), nullable=False)  # ""
    user_id = Column(String(60), ForeignKey(
        "users.id"), nullable=False)  # ""
    name = Column(String(128), nullable=False)  # ""
    description = Column(String(1024), nullable=False)  # ""
    number_rooms = Column(Integer, default=0, nullable=False)  # 0
    number_bathrooms = Column(Integer, default=0, nullable=False)  # 0
    max_guest = Column(Integer, default=0, nullable=False)  # 0
    price_by_night = Column(Integer, default=0, nullable=False)  # 0
    latitude = Column(Float)  # 0.0
    longitude = Column(Float)  # 0.0
    # amenity_ids = []  # No longer in use in db
    reviews =  relationship("Review", cascade='all, delete, delete-orphan', backref="place")

    @property
    def reviews(self):
        """"Returns cities that share state.id"""
        from models import storage

        reviewsOfPlace= []
        for object in storage.all():
            if object.__class__.__name__ == 'Review':
                if object.place_id == self.id:
                    reviewsOfPlace.append(object)
