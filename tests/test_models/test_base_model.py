#!/usr/bin/python3
""" Test for Base_Model and pep8
"""
import unittest
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """ Test pep8"""

    def test_pep8_conformance(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/base_model.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class Test_Base_Model(unittest.TestCase):
    """ Test for Base_Model
    """

    def test_instance(self):
        """ Test instances
        """
        new = BaseModel()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), BaseModel)
        self.assertEqual(type(new.id), str)

    def create_class(self):
        """ Create class
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_set_name(self):
        """ Test set name
        """
        new = BaseModel()
        new.name = "My First Model"
        self.assertEqual(new.name, "My First Model")

    def test_set_number(self):
        """ Test set number
        """
        my_model = BaseModel()
        my_model.my_number = 89
        self.assertAlmostEqual(my_model.my_number, 89)

    def test_types(self):
        """ Test types
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.to_dict(), dict)
        self.assertEqual(str, type(my_model.id))
        self.assertEqual(datetime, type(my_model.created_at))
        self.assertEqual(datetime, type(my_model.updated_at))

    def test_to_dict(self):
        """ Test to dict
        """
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json["created_at"], str)
        self.assertIsInstance(my_model_json["updated_at"], str)
        self.assertEqual(my_model_json["__class__"], "BaseModel")

    def test_to_dict_2(self):
        """ Test to dict_2
        """
        my_model = BaseModel()
        self.assertIn('id', my_model.to_dict())
        self.assertIn('created_at', my_model.to_dict())
        self.assertIn('updated_at', my_model.to_dict())

    def test_save(self):
        """ Test save
        """
        new = BaseModel()
        created = new.updated_at
        new.save()
        updated = new.updated_at
        self.assertNotEqual(updated, created)

    def test_attr(self):
        """ Test attributes of instance
        """
        new = BaseModel()
        new.algo = "cosas"
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "algo"))


if __name__ == "__main__":
    unittest.main()