# metametrics/tests/test_point.py

import unittest
from metametrics import Point

class PointTests(unittest.TestCase):

	def test_point_equality(self):
		a = Point(1,2)
		b = Point(2,1)
		self.assertNotEqual(a,b)
		c = Point(1,2)
		self.assertEqual(a,c)

if __name__ == '__main__':
    unittest.main()
