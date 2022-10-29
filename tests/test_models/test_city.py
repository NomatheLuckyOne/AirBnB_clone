#!/usr/bin/python3
"""Test City"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testcity(unittest.TestCase):

    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def test_city(self):
        """
        Test attributes of Class City
        """
        my_city = City()
        my_state = State()
        my_city.name = "Medellin"
        my_city.state_id = my_state.id
        self.assertEqual(my_city.name, 'Medellin')
        self.assertEqual(my_city.state_id, my_state.id)
