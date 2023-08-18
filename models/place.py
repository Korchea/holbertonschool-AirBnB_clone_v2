#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey(
        'cities.id'), nullable=False)  # ""
    user_id = Column(String(60), ForeignKey(
        'users.id'), nullable=False)  # ""
    name = Column(String(128), nullable=False)  # ""
    description = Column(String(1024), nullable=True)  # ""
    number_rooms = Column(Integer, default=0, nullable=False)  # 0
    number_bathrooms = Column(Integer, default=0, nullable=False)  # 0
    max_guest = Column(Integer, default=0, nullable=False)  # 0
    price_by_night = Column(Integer, default=0, nullable=False)  # 0
    latitude = Column(Float)  # 0.0
    longitude = Column(Float)  # 0.0
    amenity_ids = []  # No longer in use in db
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review", cascade='all, delete', backref="places")
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenity")
    else:
        @property
        def reviews(self):
            """ Getter for reviews in FileStorage """
            # import here to avoid circular import
            from models.review import Review
            from models import storage
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            from models import storage
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj=None):
            if type(obj) == 'Amenity' and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
