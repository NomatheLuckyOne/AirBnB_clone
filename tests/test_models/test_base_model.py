#!/usr/bin/python3
"""Unittest BaseModel class"""

import unittest
import os
from models.base_model import BaseModel
import pep8


class TEST_base(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        cls.basel = BaseModel()
        cls.basel.name = "Jocelyn"
        cls.basel.my_number = 30

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.basel
        try:
            os.remove("file.json")
        except Exception as e:
            print(e)
            pass

    def test_init(self):
        """test if the base is an instance of type BaseModel"""
        self.assertTrue(isinstance(self.basel, BaseModel))

    def test_atritt(self):
        """test if the attritt exist"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_to_dict(self):
        """test if to_dictionary method works"""
        base = BaseModel()
        base.name = "Kobe"
        base.age = 40
        convert = base.to_dict()
        self.assertEqual(convert["id"], base.id)
        self.assertEqual(convert["name"], base.name)
        self.assertEqual(convert["age"], base.age)
        self.assertEqual(convert["updated_at"], base.updated_at.isoformat())
        self.assertEqual(convert["created_at"], base.created_at.isoformat())
        self.assertEqual(convert["__class__"], type(base).__name__)

    def tets_save(self):
        """test if the save method works"""
        self.basel.save()
        self.assertNotEqual(self.basel.created_at, self.basel.updated_at)

    def test_functions(self):
        """test if the fucntions exits """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_pep8_BaseModel(self):
        """test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
