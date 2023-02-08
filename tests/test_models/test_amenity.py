#!/usr/bin/python3
"""AMENITY MODULE TESTS"""
from models.amenity import Amenity
import pep8
import unittest

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""

    def setUp(self):
        """Sets up objects for testing"""
        self.amenityOne = Amenity()
        self.amenityTwo = Amenity()

    def test_pep8(self):
        """Tests for pep8 style"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(["./models/amenity.py"])
        self.assertEqual(result.total_errors, 0)

    def test_type(self):
        """Tests the type"""
        self.assertEqual(type(self.amenityOne.name), str)
        self.assertEqual(type(self.amenityTwo.name), str)
        self.assertIsInstance(self.amenityOne, Amenity)
        self.assertIsInstance(self.amenityTwo, Amenity)

    def test_attributes(self):
        """Tests the attributes"""
        self.assertTrue(hasattr(self.amenityOne, "name"))
        self.assertFalse(hasattr(self.amenityOne, "user_id"))
        self.assertTrue(self.amenityOne.id != self.amenityTwo.id)

if __name__ == "__main__":
    unittest.main()