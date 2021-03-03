"""Binary search algorithm."""


def binary_search(collection, search_value):
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

    while first <= last:
        mid = first + ((last - first) // 2)

        if collection[mid] == search_value:
            return mid
        elif collection[mid] < search_value:
            first = mid + 1
        else:
            last = mid - 1

    return -1


def _is_continue(first, last):
    return (True if first <= last else False)


def _next_index(first, last):
    return first + ((last - first) // 2)
