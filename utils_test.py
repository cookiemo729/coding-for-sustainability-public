from utils import average, random_weighted


def test_average_single_element():
    assert average([5]) == 5, "Expected average of [5] to be 5"


def test_average_positive_numbers():
    assert average([1, 2, 3, 4, 5]) == 3, "Expected average of [1, 2, 3, 4, 5] to be 3"


def test_average_mixed_numbers():
    assert (
        average([-1, 2, -3, 4, -5]) == -0.6
    ), "Expected average of [-1, 2, -3, 4, -5] to be -0.6"


def test_random_weighted_in_range():
    low = 1
    high = 10
    outliers = 2
    result = random_weighted(low, high, outliers)
    assert low <= result <= high, "The result should be within the specified range."


def test_random_weighted_type():
    result = random_weighted(1, 10, 2)
    assert isinstance(result, int), "The result should be an integer."


def test_random_weighted_bias():
    low = 1
    high = 10
    outliers = 2
    results = [random_weighted(low, high, outliers) for _ in range(10000)]
    average_result = sum(results) / len(results)
    assert (
        average_result < (low + high) / 2
    ), "The function should be biased towards non-outliers."
