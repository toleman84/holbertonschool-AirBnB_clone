#!/usr/bin/python3
""""""
import uuid
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    def test_no_args(self):
        """"""
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_init(self):
        model = BaseModel()
        self.assertEqual(model.id, str(uuid.uuid4()))
        self.assertEqual(model.created_at, datetime.today())
        self.assertEqual(model.updated_at, datetime.today())

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str(self):
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            model.__class__.__name__, model.id, model.__dict__
        )
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertEqual(model.updated_at, datetime.today())

    def test_to_dict(self):
        model = BaseModel()
        expected_dict = {
            "id": model.id,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
            "__class__": model.__class__.__name__,
        }
        self.assertEqual(model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
