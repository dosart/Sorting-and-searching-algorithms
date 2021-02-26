"""Search algorithms."""


def linear_search(collection, search_value):
    """Return element's index if it exist in collection.

    Args:
        collection: iterable collection
        search_value: search element

    Returns:
        index: index elementa if it exist, else -1
    """
    for (index, element) in enumerate(collection):
        if element == search_value:
            return index
    return -1


def binary_search(collection, search_value):
    return -1
