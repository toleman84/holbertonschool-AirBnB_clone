#!/usr/bin/python3
import unittest
import models
from models.city import City


class TestCity(unittest.TestCase):

    def test_create_city(self):
        city = City(name="San Francisco")
        self.assertEqual(city.name, "San Francisco")

    def test_retrieve_city(self):
        city1 = City()
        city1.name = "San Francisco"
        city1.save()
        retrieved_city = models.storage.get(city1.id)
        self.assertEqual(retrieved_city.name, "San Francisco")

    def test_modify_city(self):
        city1 = City()
        city1.save()
        city1.name = "Los Angeles"
        city1.save()
        retrieved_city = models.storage.get(city1.id)
        self.assertEqual(retrieved_city.name, "Los Angeles")

    def test_delete_city(self):
        city1 = City()
        city1.name = "San Francisco"
        city1.save()
        models.storage.delete(city1)
        retrieved_city = models.storage.get(city1.id)
        self.assertIsNone(retrieved_city)
