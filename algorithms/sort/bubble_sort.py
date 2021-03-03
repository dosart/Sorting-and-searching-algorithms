"""Bubble sort algorithm."""


def bubble_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    swapped = True
    length = len(seq)

    while swapped:
        swapped = False
        for index in range(1, length):
            if seq[index - 1] > seq[index]:
                seq[index - 1], seq[index] = seq[index], seq[index - 1]
                swapped = True
