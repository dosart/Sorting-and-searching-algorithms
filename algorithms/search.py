"""Search algorithms."""


def linear_search(collection, search_value):
    """Return element's index if it exist in collection.

    Args:
        collection: iterable collection
        search_value: search element

    Returns:
        index (int): index elementa if it exist, else -1
    """
    for (index, element) in enumerate(collection):
        if element == search_value:
            return index
    return -1


def find_if(collection, predicate):
    """Return element's index if it exist in collection.

    Args:
        collection: iterable collection
        predicate (function): predicate function

    Returns:
        index (int): index elementa if it exist, else -1
    """
    for (index, element) in enumerate(collection):
        if predicate(element):
            return index
    return -1


def exponential_search(collection, search_value):
    """Return element's index if predicate is true.

    Implementation of an iterative version of the algorithm

    Args:
        collection: iterable collection
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


def binary_search(collection, search_value):
    """Return element's index if predicate is true.

    Implementation of an iterative version of the algorithm

    Args:
        collection: iterable collection
        search_value: search element

    Returns:
        index (int): index elementa if it exist, else -1
    """
    first = 0
    last = len(collection) - 1

    while first <= last:
        mid = first + ((last - first) // 2)

        if collection[mid] == search_value:
            return mid
        elif collection[mid] < search_value:
            first = mid + 1
        else:
            last = mid - 1

    return -1
