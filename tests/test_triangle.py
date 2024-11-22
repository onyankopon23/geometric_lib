import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4, 5), 6)
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()
