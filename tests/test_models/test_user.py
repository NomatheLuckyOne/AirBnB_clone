#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testuser(unittest.TestCase):

    def test_pep8_conformance_user(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_User(self):
        """
        Test attributes of Class Use
        """
        my_user = User()
        my_user.first_name = "Juan"
        my_user.last_name = "Granada"
        my_user.email = '2020@holbertonschool.com'
        self.assertEqual(my_user.first_name, "Juan")
        self.assertEqual(my_user.last_name, "Granada")
        self.assertEqual(my_user.email, '2020@holbertonschool.com')

    def test_subclass(self):
        self.assertIsNotNone(User.__doc__)
