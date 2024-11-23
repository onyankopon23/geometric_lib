import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area_positive(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(4), 16)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-4)
