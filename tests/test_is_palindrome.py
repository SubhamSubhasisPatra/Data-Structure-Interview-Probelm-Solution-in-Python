from src.recursion.is_palindrome import is_palindrome
from unittest import TestCase


class TestRecursion(TestCase):
    def test_is_palindrome(self):
        arr1 = [1, 2, 3, 2, 1]
        arr2 = [1, 2, 3, 4, 5]
        arr3 = [1, 2, 3, 3, 2, 1]
        self.assertTrue(is_palindrome(arr1, 0, len(arr1)))
        self.assertFalse(is_palindrome(arr2, 0, len(arr2)))
        self.assertTrue(is_palindrome(arr3, 0, len(arr3)))
