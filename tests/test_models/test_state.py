#!/usr/bin/python3
"""Defines test for state.py"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_state_initialization(self):
        """Test State object initialization."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

    def test_state_attributes(self):
        """Test State object attributes."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_state_to_dict_method(self):
        """Test to_dict method of State."""
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_str_method(self):
        """Test __str__ method of State."""
        state = State()
        string = str(state)
        self.assertEqual(string[:7], "[State]")
        self.assertEqual(string[-2:], "{}")


if __name__ == "__main__":
    unittest.main()

