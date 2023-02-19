import insert_sort
import pytest


# Define a fixture that provides a list of sorting functions to test
@pytest.fixture
def sorting_functions():
    return [insert_sort.sort]


# Define a table-driven test case with multiple scenarios
@pytest.mark.parametrize("sorting_func", sorting_functions())
def test_sorting(sorting_func):
    # Define test cases with custom names
    test_cases = [
        ([], [], "empty list"),
        ([5], [5], "single-item list"),
        ([5, 3, 8, 1, 2, 7, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8], "multiple items")
    ]
    # Test each scenario
    for input_data, expected_output, name in test_cases:
        assert sorting_func(input_data) == expected_output, f"{name} failed"
