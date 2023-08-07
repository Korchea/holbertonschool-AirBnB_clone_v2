#!/usr/bin/python3
"""test for amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """test the Amenity class"""

    @classmethod
    def set_up(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Tv"

    def test_attributes(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_attribute_types(self):
        """test"""
        self.assertEqual(type(self.amenity.name), str)

    def test_is_subclass(self):
        """test"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_save(self):
        """test"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()