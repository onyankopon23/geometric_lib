import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):

    def test_calc_circle_area_positive(self):
        self.assertAlmostEqual(calc('circle', 'area', [5]), 78.53981633974483)

    def test_calc_square_perimeter_positive(self):
        self.assertEqual(calc('square', 'perimeter', [4]), 16)

    def test_calc_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc('hexagon', 'area', [5])

    def test_calc_invalid_function(self):
        with self.assertRaises(ValueError):
            calc('circle', 'volume', [5])

    def test_calc_invalid_parameters(self):
        with self.assertRaises(ValueError):
            calc('circle', 'area', [5, 10])
