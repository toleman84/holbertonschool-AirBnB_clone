import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_create_amenity(self):
        amenity = Amenity(name="Wifi")
        self.assertEqual(amenity.name, "Wifi")

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

if __name__ == '__main__':
    unittest.main()