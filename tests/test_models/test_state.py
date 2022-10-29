#!/usr/bin/python3
"""
module contains test
for state
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class TestState(unittest.TestCase):

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_father(self):
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')
