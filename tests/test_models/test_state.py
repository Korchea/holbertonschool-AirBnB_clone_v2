#!/usr/bin/python3
"""test for state"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """test the State class"""

    @classmethod
    def setUpClass(cls):
        """set up"""
        cls.state = State()
        cls.state.name = "Canelones"

    def test_attributes_State(self):
        """chekcing if State have attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """test"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """test"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """test"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """test"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()