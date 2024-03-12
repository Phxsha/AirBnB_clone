#!/usr/bin/python3
"""Defines test for user class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def test_instance_creation(self):
        """Test creating an instance of User"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attributes(self):
        """Test the default attribute values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_representation(self):
        """Test the __str__ method"""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], user.email)
        self.assertEqual(user_dict['password'], user.password)
        self.assertEqual(user_dict['first_name'], user.first_name)
        self.assertEqual(user_dict['last_name'], user.last_name)

    def test_from_dict_method(self):
        """Test creating an instance from a dictionary"""
        user_dict = {
            '__class__': 'User',
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**user_dict)
        self.assertEqual(user.id, '123')
        self.assertEqual(str(user.created_at), '2023-01-01 00:00:00')
        self.assertEqual(str(user.updated_at), '2023-01-01 00:00:00')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')


if __name__ == '__main__':
    unittest.main()

