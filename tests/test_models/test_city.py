#!/usr/bin/python3
""" Module used to test city """


import unittest
import models
from models.city import City
from time import sleep
from datetime import datetime


class Testcity(unittest.TestCase):

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_create_city(self):
        city = City(name="Toledo")
        self.assertEqual(city.name, "Toledo")

    def test_two_cities_unique_ids(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_retrieve_city(self):
        c1 = City()
        c1.name = "Madrid"
        c1.save()
        retrieved_city = models.storage.get(c1.id)
        self.assertEqual(retrieved_city.name, "Madrid")

    def test_modify_city(self):
        c1 = City()
        c1.name = "San Francisco"
        c1.save()
        c1.name = "Los Angeles"
        c1.save()
        retrieved_city = models.storage.get(c1.id)
        self.assertEqual(retrieved_city.name, "Los Angeles")

    def test_delete_city(self):
        city = City()
        city.name = "San Francisco"
        city.save()
        models.storage.delete(city)
        retrieved_city = models.storage.get(city.id)
        self.assertIsNone(retrieved_city)

    def test_two_cities_different_created_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_two_cities_different_updated_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        c1 = City()
        c1.id = "123"
        c1.created_at = c1.updated_at = dt
        cstring = c1.__str__()
        self.assertIn("[City] (123)", cstring)
        self.assertIn("'id': '123'", cstring)
        self.assertIn("'created_at': " + dt_repr, cstring)
        self.assertIn("'updated_at': " + dt_repr, cstring)


if __name__ == '__main__':
    unittest.main()
