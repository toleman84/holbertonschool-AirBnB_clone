#!/usr/bin/python3
""""""
import models
import unittest
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from console import HBNBCommand
from unittest.mock import patch


class TestFileStorage(unittest.TestCase):

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == '__main__':
    unittest.main()
