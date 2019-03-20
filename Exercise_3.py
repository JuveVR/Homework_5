import unittest
from Homework_3.Exercise_6 import is_year_leap,triangle_existance,triangle_type

class LeapTest(unittest.TestCase):
    def test_leap(self):
        leap = is_year_leap(2000)
        self.assertTrue(leap)
    def test_not_leap(self):
        not_leap = is_year_leap(2001)
        self.assertFalse(not_leap)

class TriangleExist(unittest.TestCase):
    def test_exist(self):
        exist = triangle_existance(4,4,3)
        self.assertEqual(exist, True)
    def test_not_exist(self):
        not_exist = triangle_existance(1,2,24)
        self.assertFalse(not_exist)

class TriangleType(unittest.TestCase):
    def test_equilateral(self):
        equil = triangle_type(15,15,15)
        self.assertEqual(equil,"Equilateral triangle")
    def test_isosceles(self):
        iso = triangle_type(1,15,15)
        self.assertEqual(iso, "Isosceles triangle")
    def test_versatile(self):
        vers = triangle_type(4,5,6)
        self.assertEqual(vers, "Versatile triangle")
    def test_not_exist(self):
        not_exist = triangle_type(0,0,0)
        self.assertEqual(not_exist, "This triangle does not exist")
    def test_not_exist2(self):
        not_exist = triangle_type(1, 2, 3)
        self.assertEqual(not_exist, "This triangle does not exist")




