#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import json
from os import environ
from os import getenv
import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """Storage Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """"Initializes Instance Values"""
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            environ['HBNB_MYSQL_USER'],
            environ['HBNB_MYSQL_PWD'],
            environ['HBNB_MYSQL_HOST'],
            environ['HBNB_MYSQL_DB'],
            pool_pre_ping=True))
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current db all objects/all objects of class name"""
        diccionario = {}
        if cls is None:
            pass
        else:
            objetos = self.__session.query(cls).all()

        for objet in objetos:
            key = f"{objet.__class__.__name__}.{objet.id}"
            diccionario[key] = objet
        return (diccionario)

    def new(self, obj):
        """Adds the object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves to current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from current database session"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Create all tables in databases"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()
