#!/usr/bin/python3
"""Defines test for city class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_city_initialization(self):
        """Test City object initialization."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attributes(self):
        """Test City object attributes."""
        city = City()
        city.state_id = "123"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "San Francisco")

    def test_city_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))

    def test_city_to_dict_method(self):
        """Test to_dict method of City."""
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_str_method(self):
        """Test __str__ method of City."""
        city = City()
        string = str(city)
        self.assertEqual(string[:7], "[City]")
        self.assertEqual(string[-2:], "{}")


if __name__ == "__main__":
    unittest.main()

