import insert_sort
import quick_sort

test_cases = [
    ([], [], "empty list"),
    ([5], [5], "single-item list"),
    ([5, 3, 8, 1, 2, 7, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8], "multiple items")
]


def helper(func):
    for input_data, expected, name in test_cases:
        assert func.sort(input_data) == expected, f"{name} failed"


def test_insert_sort():
    helper(insert_sort)


def test_quick_sort():
    helper(quick_sort)
