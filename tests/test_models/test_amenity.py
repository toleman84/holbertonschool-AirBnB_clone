#!/usr/bin/python3
""" Module used to test amenities """


import unittest
import models
from models.amenity import Amenity
from time import sleep
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_create_amenity(self):
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")

    def test_two_amenities_unique_ids(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_retrieve_amenity(self):
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity.save()
        retrieved_amenity = models.storage.get(amenity.id)
        self.assertEqual(retrieved_amenity.name, "Wifi")

    def test_modify_amenity(self):
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity.save()
        amenity.name = "Air Conditioning"
        amenity.save()
        retrieved_amenity = models.storage.get(amenity.id)
        self.assertEqual(retrieved_amenity.name, "Air Conditioning")

    def test_delete_amenity(self):
        amenity = Amenity()
        amenity.name = "Wifi"
        amenity.save()
        models.storage.delete(amenity)
        retrieved_amenity = models.storage.get(amenity.id)
        self.assertIsNone(retrieved_amenity)

    def test_two_amenities_different_created_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123"
        am.created_at = am.updated_at = dt
        amstring = am.__str__()
        self.assertIn("[Amenity] (123)", amstring)
        self.assertIn("'id': '123'", amstring)
        self.assertIn("'created_at': " + dt_repr, amstring)
        self.assertIn("'updated_at': " + dt_repr, amstring)

if __name__ == '__main__':
    unittest.main()
