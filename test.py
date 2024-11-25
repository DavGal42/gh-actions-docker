import unittest

from main import add, subtract, multiply, divide, floor_divide, modulus

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_floor_divide(self):
        self.assertEqual(floor_divide(10, 3), 3)
        self.assertEqual(floor_divide(-10, 3), -4)
        with self.assertRaises(ValueError):
            floor_divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(-10, 3), 2)
        with self.assertRaises(ValueError):
            modulus(10, 0)

if __name__ == "__main__":
    unittest.main()