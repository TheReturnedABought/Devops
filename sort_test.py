import unittest

# Assuming all the sorting functions are already defined in this file

class TestSortingAlgorithms(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(bubble_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([3, 3, 3]), [3, 3, 3])

    def test_quick_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(quick_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([3, 3, 3]), [3, 3, 3])

    def test_merge_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(merge_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([3, 3, 3]), [3, 3, 3])

    def test_insertion_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(insertion_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([3, 3, 3]), [3, 3, 3])

    def test_selection_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(selection_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([3, 3, 3]), [3, 3, 3])

    def test_heap_sort(self):
        arr = [5, 3, 8, 6, 2]
        self.assertEqual(heap_sort(arr), [2, 3, 5, 6, 8])
        self.assertEqual(heap_sort([]), [])
        self.assertEqual(heap_sort([1]), [1])
        self.assertEqual(heap_sort([3, 3, 3]), [3, 3, 3])


if __name__ == "__main__":
    unittest.main()
