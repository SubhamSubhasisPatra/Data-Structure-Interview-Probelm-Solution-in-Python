from unittest import TestCase
from src.recursion.subsequence import find_subsets


class TestRecursion(TestCase):
    def test_find_subsets_empty_array(self):
        input_arr = []
        n = len(input_arr)
        expected_output = [[]]
        self.assertCountEqual(find_subsets(0, [], input_arr, n), expected_output)

    def test_find_subsets_single_element_array(self):
        input_arr = [1]
        n = len(input_arr)
        expected_output = [[], [1]]
        self.assertCountEqual(find_subsets(0, [], input_arr, n), expected_output)

    def test_find_subsets_two_element_array(self):
        input_arr = [1, 2]
        n = len(input_arr)
        expected_output = [[], [2], [1], [1, 2]]
        self.assertCountEqual(find_subsets(0, [], input_arr, n), expected_output)

    def test_find_subsets_three_element_array(self):
        input_arr = [3, 1, 2]
        n = len(input_arr)
        expected_output = [[], [2], [1], [1, 2], [3], [3, 2], [3, 1], [3, 1, 2]]
        self.assertCountEqual(find_subsets(0, [], input_arr, n), expected_output)

    def test_find_subsets_duplicate_elements(self):
        input_arr = [1, 2, 2]
        n = len(input_arr)
        expected_output = [[1, 2, 2], [1, 2], [1, 2], [1], [2, 2], [2], [2], []]
        self.assertCountEqual(find_subsets(0, [], input_arr, n), expected_output)
