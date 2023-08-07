#!/usr/bin/python3
"""test for city"""
import unittest
from os import getenv
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """test the city class"""

    @classmethod
    def set_up(cls):
        """set up"""
        cls.city = City()
        cls.city.name = "San Jacinto"
        cls.city.state_id = "Canelones"

    def test_checking_for_docstring_City(self):
        """test"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_to_dict_City(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()