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
    """Return element's index if predicate is true.

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
