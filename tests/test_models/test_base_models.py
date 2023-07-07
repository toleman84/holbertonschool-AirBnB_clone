#!/usr/bin/python3
""" Module used to test  the base model """
import uuid
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ Test class for base model """

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_init(self):
        model = BaseModel()
        self.assertNotEqual(model.id, str(uuid.uuid4()))
        self.assertEqual(str(type(model)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(issubclass(type(model), BaseModel))

    def test_no_args(self):
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertEqual(base.__class__.__name__, "BaseModel")

    def test_id(self):
        w = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(w)), len(w))

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_checking_for_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_str(self):
        datet = datetime.today()
        datet_repr = repr(datet)
        bm = BaseModel()
        bm.id = "123"
        bm.created_at = bm.updated_at = datet
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123)", bmstr)
        self.assertIn("'id': '123'", bmstr)
        self.assertIn("'created_at': " + datet_repr, bmstr)
        self.assertIn("'updated_at': " + datet_repr, bmstr)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, datetime.today())
        self.assertIsNotNone(model.updated_at)
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)
        self.assertLess(self.base_model.created_at,
                            self.base_model.updated_at)
    
    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_time_updated = bm.updated_at
        bm.save()
        second_time_updated = bm.updated_at
        self.assertLess(first_time_updated, second_time_updated)
        sleep(0.05)
        bm.save()
        self.assertLess(second_time_updated, bm.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        expected_dict = {
            "id": model.id,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
            "__class__": model.__class__.__name__,
        }
        base1_dict = self.base_model.to_dict()
        self.assertEqual(model.to_dict(), expected_dict)
        self.assertEqual(self.base_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
