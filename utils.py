import random


def average(list):
    """
    Calculate the average of a list of numbers.
    """
    if len(list) == 0:
        return 0

    return sum(list) / len(list)


def random_weighted(low, high, outliers, weight=10_000):
    """
    Generate a random number between low and high with weights against the outliers.

    Args:
        low (int): the lower bound of the random number
        high (int): the upper bound of the random number
        outliers (int): the number of outliers on the high end
        weight (int): the weight of the non-outliers
    """
    values = list(range(low, high + 1))
    weights = [1] * len(values)
    weight_max = len(weights) - outliers
    weights[0:weight_max] = [weight] * weight_max
    choices = random.choices(values, weights=weights, k=1)
    return choices[0]
