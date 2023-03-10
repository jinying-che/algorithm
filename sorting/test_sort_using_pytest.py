import insert_sort
import quick_sort
import merge_sort
import merge_sort_with_less_space
import heap_sort


test_cases = [
    ([], [], "empty list case"),
    ([5], [5], "single-item list case"),
    ([5, 3, 8, 1, 2, 7, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8], "multiple items case")
]


def helper(func):
    for input_data, expected, name in test_cases:
        assert func.sort(input_data) == expected, f"{name} failed"


def test_insert_sort():
    helper(insert_sort)


def test_quick_sort():
    helper(quick_sort)


def test_merge_sort():
    helper(merge_sort)


def test_merge_sort_with_less_space():
    helper(merge_sort_with_less_space)


def test_heap_sort():
    helper(heap_sort)
