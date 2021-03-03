"""Exponential search algorithm."""

from algorithms.search.binary_search import binary_search


def exponential_search(collection, search_value):
    """Return element's index if predicate is true.

    Implementation of an iterative version of the algorithm

    Args:
        collection: sorted indexed collection
        search_value: search element

    Returns:
        index (int): index elementa if it exist, else -1
    """
    length = len(collection)

    if length == 0:
        return -1

    if collection[0] == search_value:
        return 0

    index = 1
    while index < length and collection[index] <= search_value:
        index *= 2
    return binary_search(collection[:index], search_value)
