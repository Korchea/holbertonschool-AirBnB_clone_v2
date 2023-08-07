#!/usr/bin/python3
"""test for file storage"""
import unittest
from os import getenv
import MySQLdb
from models.base_model import Base
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """test the DBStorage"""

    @classmethod
    def set_up(self):
        """set up"""
        self.User = getenv("HBNB_MYSQL_USER")
        self.Passwd = getenv("HBNB_MYSQL_PWD")
        self.Db = getenv("HBNB_MYSQL_DB")
        self.Host = getenv("HBNB_MYSQL_HOST")
        self.db = MySQLdb.connect(host=self.Host, user=self.User,
                                  passwd=self.Passwd, db=self.Db,
                                  charset="utf8")
        self.query = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

if __name__ == "__main__":
    unittest.main()