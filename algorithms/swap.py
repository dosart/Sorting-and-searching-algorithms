"""Implementation swap function."""


def swap(array, one, two):
    """Take two elements in array and exchange it.

    Args:
        array (list): indexed collection
        one (int): first element index for exchange
        two (int): srcond element index for exchange
    """
    array[one], array[two] = array[two], array[one]
