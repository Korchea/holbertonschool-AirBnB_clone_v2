#!/usr/bin/python3
"""Son todos los test que se me ocurrieron para probar el file_storage
"""
import unittest
import os
import json
import pep8
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestCodeFormat(unittest.TestCase):
    """test pep8"""

    def test_pep8_conformance(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_engine/test_file_storage.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class TestFileStorage(unittest.TestCase):
    """Son todos los test que se me ocurrieron para probar el file_storage
    """

    def create(self):
        """Create an FileStorage
        """
        self.storage = FileStorage()
        self.path = "file.json"

    def remove(self):
        """Remuve a file
        """
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_all_empty(self):
        """Test the function all empty
        """
        self.assertAlmostEqual(self.storage.all(), {})

    def test_new(self):
        """Test function new
        """
        my_model = BaseModel()
        self.storage.new(my_model)
        k = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertAlmostEqual(len(self.storage.all()), 1)
        self.assertAlmostEqual(k in self.storage.all(), True)

    def test_save(self):
        """Test save
        """
        my_model = BaseModel()
        self.storage.save()
        self.assertAlmostEqual(os.path.exists(self.path), True)
        with open(self.path, mode="r") as file:
            text = json.load(file)
        k = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertAlmostEqual(k in text, True)

    def test_file_path(self):
        """Test the file path
        """
        self.assertAlmostEqual(
            self.storage._FileStorage__file_path, "file.json")

    def test_storage_contains_dict(self):
        """Test storage contains dict
        """
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_file_is_str(self):
        """Test if file is a str
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_reload_2(self):
        """Test reload 2"""
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        with open(self.path, "r") as file:
            data = json.load(file)
        data["BaseModel.111111"] = {"id": "111111",
                                    "__class__": "BaseModel",
                                    "name": "my_model",
                                    "created_at": "2023-07-06T14:21:32.911051",
                                    "updated_at": "2023-07-06T14:21:32.911057"}
        with open(self.path, "w") as file:
            json.dump(data, file)
        self.storage.reload()
        self.assertIn("BaseModel.111111", self.storage.all())
        my_model = self.storage.all()["BaseModel.111111"]
        self.assertEqual(my_model.id, "111111")
        self.assertEqual(my_model.name, "my_model")

    def test_reload(self):
        """Test reload
        """
        my_model = BaseModel()
        self.storage.save()
        my_json = self.storage.all()
        self.assertEqual(len(my_json), 2)
        for k in my_json.keys():
            self.assertTrue(isinstance(my_json[k], BaseModel))

    def test_reload_file_not_exists(self):
        """
        Test reload when the JSON file does not exist
        """
        self.remove()
        self.storage.reload()
        self.assertAlmostEqual(len(self.storage.all()), 0)

    def test_reload_empty_file(self):
        """
        Test reload when the JSON file is empty
        """
        with open(self.path, "w") as file:
            file.write("")
        self.storage.reload()
        self.assertAlmostEqual(len(self.storage.all()), 0)

    def test_reload_invalid_json(self):
        """
        Test reload when the JSON file contains invalid JSON
        """
        with open(self.path, "w") as file:
            file.write("{invalid_json}")
        self.storage.reload()
        self.assertAlmostEqual(len(self.storage.all()), 0)

    def test_save_no_permission(self):
        """
        Test save when there is no write permission to the JSON file
        """
        os.chmod(self.path, 0o444)
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()


if __name__ == "__main__":
    unittest.main()