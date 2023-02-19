import unittest
import insert_sort


class TestSort(unittest.TestCase):
    def test_insert_sort(self):
        test_cases = [
            ([], [], "empty"),
            ([1], [1], "single"),
            ([3, 2, 1], [1, 2, 3], "multiple")
        ]
        for input_data, ret, name in test_cases:
            with self.subTest(name):
                self.assertListEqual(ret, insert_sort.sort(input_data))


if __name__ == '__main__':
    unittest.main(verbosity=2)
