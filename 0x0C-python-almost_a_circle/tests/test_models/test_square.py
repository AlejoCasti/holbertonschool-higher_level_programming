#!/usr/bin/python3
import unittest
from models.base import Base

class testBase(unittest.TestCase):
    
    def test_add(self):
        ex = Base()
        self.assertEqual(ex.id, 1)
        ex = Base(38)
        self.assertEqual(ex.id, 38)
        ex = Base()
        self.assertEqual(ex.id, 2)
        ex = Base(3.2)
        self.assertEqual(ex.id, 3.2)
        ex = Base(-1)
        self.assertEqual(ex.id, -1)
        ex = Base([1, 2, 3])
        self.assertEqual(ex.id, [1, 2, 3])
        ex = Base(True)
        self.assertEqual(ex.id, True)
        ex = Base({'pru': 1})
        self.assertEqual(ex.id, {'pru': 1})
        ex = Base((1, ))
        self.assertEqual(ex.id, (1, ))
        ex = Base()
        self.assertEqual(ex.id, 3)

    def test_tjs(self):
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        failure_msg = 'object of type \'int\' has no len()'
        self.assertTrue(Base.to_json_string(1), msg=failure_msg)
        

if __name__ == '__main__':
    unittest.main()
