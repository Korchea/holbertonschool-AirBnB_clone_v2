#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)  # ""
    cities = relationship("City",
                        cascade="all, delete, delete-orphan", backref="state")

    @property
    def cities(self):
        """"Returns cities that share state.id"""
        from models import storage

        citiesInState = []
        for object in storage.all():
            if object.__class__.__name__ == 'City':
                if object.state_id == self.id:
                    citiesInState.append(object)
