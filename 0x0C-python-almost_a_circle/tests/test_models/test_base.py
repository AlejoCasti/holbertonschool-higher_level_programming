#!/usr/bin/python3
"""
Unittest for Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys
import os


class TestBase(unittest.TestCase):
    """
    class TestBase
    """

    def test_class(self):
        b0 = Base()
        self.assertTrue(isinstance(b0, Base))

    def test_nb(self):
        b0 = Base()
        self.assertTrue(hasattr(b0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_id(self):
        b0 = Base()
        self.assertTrue(hasattr(b0, 'id'))
        Base._Base__nb_objects = 0

    def test_automatic(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b5 = Base()
        self.assertEqual(b5.id, 5)
        Base._Base__nb_objects = 0

    def test_manual(self):
        b1 = Base(45)
        self.assertEqual(b1.id, 45)
        b2 = Base(56)
        self.assertEqual(b2.id, 56)
        b3 = Base(67)
        self.assertEqual(b3.id, 67)
        b4 = Base(78)
        self.assertEqual(b4.id, 78)
        b5 = Base(89)
        self.assertEqual(b5.id, 89)
        Base._Base__nb_objects = 0

    def test_mixed(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(56)
        self.assertEqual(b2.id, 56)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(78)
        self.assertEqual(b4.id, 78)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_base_instance(self):
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_base_attr_id_exists(self):
        obj = Base()
        failure_msg = 'property id not found'
        self.assertTrue(hasattr(obj, 'id'), msg=failure_msg)

    def test_base_nb_objects_exists(self):
        obj = Base()
        failure_msg = 'global var __nb_objects not found'
        self.assertTrue(hasattr(obj, '_Base__nb_objects'), msg=failure_msg)
