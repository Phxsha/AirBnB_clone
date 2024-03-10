#!/usr/bin/python3
"""Unittests for models/base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_base_model_creation(self):
        """Test creation of BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_base_model_str(self):
        """Test string representation of BaseModel instance."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_base_model_save(self):
        """Test saving BaseModel instance."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """Test converting BaseModel instance to dictionary."""
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 42
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)

    def test_base_model_new(self):
        """Test adding new BaseModel instance to storage."""
        my_model = BaseModel()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertNotIn(key, BaseModel._BaseModel__objects)
        my_model.save()
        self.assertIn(key, BaseModel._BaseModel__objects)


if __name__ == '__main__':
    unittest.main()

