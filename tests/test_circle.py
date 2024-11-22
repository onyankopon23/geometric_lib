import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)
        with self.assertRaises(ValueError):
            area(-3)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)
        with self.assertRaises(ValueError):
            perimeter(-3)

if __name__ == "__main__":
    unittest.main()
