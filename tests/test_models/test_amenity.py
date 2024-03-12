#!/usr/bin/python3
"""Defines unittests for amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_amenity_initialization(self):
        """Test Amenity object initialization."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_amenity_attributes(self):
        """Test Amenity object attributes."""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")

    def test_amenity_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_amenity_to_dict_method(self):
        """Test to_dict method of Amenity."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_str_method(self):
        """Test __str__ method of Amenity."""
        amenity = Amenity()
        string = str(amenity)
        self.assertEqual(string[:9], "[Amenity]")
        self.assertEqual(string[-2:], "{}")


if __name__ == "__main__":
    unittest.main()

