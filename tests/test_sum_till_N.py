from src.recursion.sum_till_N import find_total

from unittest import TestCase


class TestRecursion(TestCase):
    def test_find_total(self):
        self.assertEqual(find_total(0), 0)
        self.assertEqual(find_total(1), 1)
        self.assertEqual(find_total(2), 3)
        self.assertEqual(find_total(5), 15)
        self.assertEqual(find_total(10), 55)
