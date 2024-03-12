#!/usr/bin/python3
"""Defines tests for review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_review_initialization(self):
        """Test Review object initialization."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes(self):
        """Test Review object attributes."""
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place to stay!")

    def test_review_inherited_attributes(self):
        """Test inherited attributes from BaseModel."""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))

    def test_review_to_dict_method(self):
        """Test to_dict method of Review."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_review_str_method(self):
        """Test __str__ method of Review."""
        review = Review()
        string = str(review)
        self.assertEqual(string[:8], "[Review]")
        self.assertEqual(string[-2:], "{}")


if __name__ == "__main__":
    unittest.main()

