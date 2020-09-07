
__author__ = "sondos with help from gabby and shanquel"

import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 1), 3)
        self.assertEqual(katas.add(-8, 4), -4)
        self.assertEqual(katas.add(120, 16), 136)

    def test_multiply(self):
        self.assertEqual(katas.multiply(5, 7), 35)
        self.assertEqual(katas.multiply(-8, 4), -32)
        self.assertEqual(katas.multiply(4, 4), 16)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(3, 3), 27)
        self.assertEqual(katas.power(5, 2), 25)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(3), 6)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(15), 377)
        self.assertEqual(katas.fibonacci(8), 13)
        self.assertEqual(katas.fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
