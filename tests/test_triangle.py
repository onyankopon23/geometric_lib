import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(area(3, 4, 5), 6)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
