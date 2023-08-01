#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import json
from os import environ
import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """Storage Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """"Initializes Instance Values"""
        self.__engine = db.create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            environ.HBNB_MYSQL_USER,
            environ.HBNB_MYSQL_PWD,
            environ.HBNB_MYSQL_HOST,
            environ.HBNB_MYSQL_DB,
            pool_pre_ping=True))
        if environ.HBNB_ENV == 'test':
            db.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current db all objects/all objects of class name"""
        classes = ["BaseModel", "City", "Place", "Amenity", "Review", "State", "User"]
        if cls is not None:
          results = self.__session.query(cls).all()
          dictionary = {}
          key = ""
          for result in results:
                key = str(result.name) + '.' + str(result.id)
                dictionary.update({key: result})
          return dictionary
        else:
            for clas in classes:
                results = self.__session.query(clas).all()  # loop query through all 7 possible classes
                key = str(results.name) + '.' + str(results.id)
                dictionary.update({key: result})
            return dictionary

    def new(self, obj):
      """Adds the object to current database session"""
      self.__session.add(obj)
      self.save()

    def save(self):
      """Saves to current session"""
      self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from current database session"""
        if obj is not None:
          self.__session.remove(obj)