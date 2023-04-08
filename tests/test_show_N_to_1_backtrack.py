from io import StringIO
from unittest import TestCase
from src.recursion.show_N_to_1_backtrack import show_number


class TestRecursion(TestCase):
    def test_show_number(self):
        with StringIO() as captured_output:
            show_number(1, 3, buffer=captured_output)
            self.assertEqual(captured_output.getvalue(), "3\n2\n1\n")
