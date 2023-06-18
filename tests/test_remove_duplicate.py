from unittest import TestCase
from src.Array.remove_duplicate import remove_duplicates


class TestRemoveDuplicates(TestCase):
    def test_with_array_of_zeros_and_ones(self):
        arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 9
        self.assertEqual(expected, remove_duplicates(arr))

    def test_with_empty_array(self):
        arr = []
        expected = 0
        self.assertEqual(expected, remove_duplicates(arr))

    def test_with_array_without_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        expected = 5
        self.assertEqual(expected, remove_duplicates(arr))

    def test_with_array_of_only_duplicates(self):
        arr = [1, 1, 1, 1, 1, 1]
        expected = 2
        self.assertEqual(expected, remove_duplicates(arr))

    def test_with_large_array(self):
        arr = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 7, 8, 8, 8, 9, 9, 10]
        expected = 16
        self.assertEqual(expected, remove_duplicates(arr))
