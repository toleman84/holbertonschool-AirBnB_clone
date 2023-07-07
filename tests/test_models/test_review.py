#!/usr/bin/python3
""" Module used to test review """


import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute_types(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()