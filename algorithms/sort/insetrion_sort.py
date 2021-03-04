"""Insetrion sort algorithm."""


def insetrion_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    length = len(seq)

    for index in range(1, length):
        cursor = index
        while cursor > 0 and seq[cursor - 1] > seq[cursor]:
            seq[cursor], seq[cursor - 1] = seq[cursor - 1], seq[cursor]
            cursor = cursor - 1
