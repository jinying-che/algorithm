import insert_sort


def test_sorting():
    # Define test cases with custom names
    test_cases = [
        ([], [], "empty list"),
        ([5], [5], "single-item list"),
        ([5, 3, 8, 1, 2, 7, 4, 6], [1, 2, 3, 4, 5, 6, 7, 8], "multiple items")
    ]
    # Test each scenario
    for input_data, expected_output, name in test_cases:
        assert insert_sort.sort(input_data) == expected_output, f"{name} failed"
