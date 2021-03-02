"""Interpolation search algorithm."""


def interpolation_search(collection, search_value):
    """Return element's index if predicate is true.

    Implementation of an iterative version of the algorithm

    Args:
        collection: sorted indexed collection
        search_value: search element

    Returns:
        index (int): index elementa if it exist, else -1
    """
    first = 0
    last = len(collection) - 1

    while first <= last and search_value >= collection[first] and search_value <= collection[last]:
        index = first + int(((last - first) / (collection[last] - collection[first])) * (search_value - collection[first]))

        if collection[index] == search_value:
            return index
        elif collection[index] < search_value:
            first = index + 1
        else:
            last = index - 1

    return -1
