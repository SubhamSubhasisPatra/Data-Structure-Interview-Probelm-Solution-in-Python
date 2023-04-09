from unittest import TestCase
from src.recursion.reverse_array import reverse, single_var_swap


class TestRecursion(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse(['a', 'b', 'c'], 0, 2), ['c', 'b', 'a'])
        self.assertEqual(reverse([1, 2, 3, 4, 5], 0, 4), [5, 4, 3, 2, 1])
        self.assertEqual(reverse([], 0, 0), [])
        self.assertEqual(reverse(['a'], 0, 0), ['a'])

    def test_single_var_swap(self):
        self.assertEqual(single_var_swap(['a', 'b', 'c'], 0, 3), ['c', 'b', 'a'])
        self.assertEqual(single_var_swap([1, 2, 3, 4, 5], 0, 5), [5, 4, 3, 2, 1])
        self.assertEqual(single_var_swap([], 0, 0), [])
        self.assertEqual(single_var_swap(['a'], 0, 1), ['a'])
