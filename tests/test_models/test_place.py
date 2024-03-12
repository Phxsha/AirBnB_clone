#!/usr/bin/python3
"""Defines tests for place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_place_initialization(self):
        """Test Place object initialization."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attributes(self):
        """Test Place object attributes."""
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage by the sea"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["789"]
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.user_id, "456")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description, "A charming cottage by the sea")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["789"])

    def test_place_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))

    def test_place_to_dict_method(self):
        """Test to_dict method of Place."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_str_method(self):
        """Test __str__ method of Place."""
        place = Place()
        string = str(place)
        self.assertEqual(string[:7], "[Place]")
        self.assertEqual(string[-2:], "{}")


if __name__ == "__main__":
    unittest.main()

