from src.recursion.fibonacci import nth_fibonacci
from unittest import TestCase


class TestRecursion(TestCase):
    def test_nth_fibonacci(self):
        # test base cases
        self.assertEqual(nth_fibonacci(0), 1)
        self.assertEqual(nth_fibonacci(1), 1)

        # test some other cases
        self.assertEqual(nth_fibonacci(2), 2)
        self.assertEqual(nth_fibonacci(3), 3)
        self.assertEqual(nth_fibonacci(4), 5)
        self.assertEqual(nth_fibonacci(5), 8)
        self.assertEqual(nth_fibonacci(6), 13)
        self.assertEqual(nth_fibonacci(7), 21)
        self.assertEqual(nth_fibonacci(8), 34)
