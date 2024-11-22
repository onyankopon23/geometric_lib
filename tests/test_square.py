import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        with self.assertRaises(ValueError):
            perimeter(-4)

if __name__ == "__main__":
    unittest.main()
