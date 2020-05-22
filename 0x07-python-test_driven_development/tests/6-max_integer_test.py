#!/usr/bin/python3
"""Unittest max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests max_integer"""

    def test_empty_list(self):
        """ Empty list """
        self.assertEqual(max_integer([]), None)

    def test_normal(self):
        """ normal test """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_arg(self):
        """ no arguments """
        self.assertEqual(max_integer(), None)

    def test_emp(self):
        """ no arguments """
        self.assertEqual(max_integer(['a', 'b']), 'b')

    def test_wrong_type_list(self):
        """ wrong type data of list """
        with self.assertRaises(TypeError):
            max_integer([1, 'casa'])

    def test_wrong_args(self):
        """ wrong type data of list """
        with self.assertRaises(TypeError):
            max_integer(1)

   
if __name__ == '__main__':
    unittest.main()
