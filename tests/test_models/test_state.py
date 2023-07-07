#!/usr/bin/python3
""""""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_attributes(self):
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_attribute_types(self):
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
