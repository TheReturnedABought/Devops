import sort
import unittest

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.test_cases = [
            ([], []),  # Empty array
            ([1], [1]),  # Single element
            ([2, 1], [1, 2]),  # Two elements
            ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),  # General case
            ([3, 3, 3], [3, 3, 3]),  # All elements same
            ([10, -1, 2, 5, 0, -3], [-3, -1, 0, 2, 5, 10]),  # Mixed positive and negative
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reversed order
        ]

    def test_bubble_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual(sort.bubble_sort(input_arr[:]), expected)  # Use input_arr[:] to avoid modifying original

    def test_quick_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual(sort.quick_sort(input_arr[:]), expected)

    def test_merge_sort(self):
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr, expected=expected):
                self.assertEqual((input_arr[:]), expected)

if __name__ == "__main__":
    unittest.main()