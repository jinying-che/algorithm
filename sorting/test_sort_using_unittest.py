import unittest
import insert_sort
import quick_sort


class TestSort(unittest.TestCase):
    test_cases = [
            ([], [], "empty"),
            ([1], [1], "single"),
            ([3, 2, 1], [1, 2, 3], "multiple")
        ]

    def helper(self, func):
        for input_data, ret, name in self.test_cases:
            with self.subTest(name):
                self.assertListEqual(ret, func.sort(input_data))

    def test_insert_sort(self):
        self.helper(insert_sort)

    def test_quick_sort(self):
        self.helper(quick_sort)


if __name__ == '__main__':
    unittest.main()
