#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        from models import storage
        lista = []
        for x, y in storage._FileStorage__objects.items():
            split = x.split(".")
            if split[0] == "City":
                lista.append(y)
        filt = list(
            filter(lambda a: a.state_id == self.id, lista))
        return filt
