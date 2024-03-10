#!/usr/bin/python3
"""Define unitests for models/engine/file_storage.py"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_initialization(self):
        """Test initialization of FileStorage class."""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')

    def test_file_storage_save(self):
        """Test saving objects to file."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        self.storage.new(my_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_file_storage_reload(self):
        """Test reloading objects from file."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        self.storage.new(my_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn("BaseModel.{}".format(my_model.id), new_storage.all())


if __name__ == '__main__':
    unittest.main()

