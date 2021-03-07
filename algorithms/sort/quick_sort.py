"""Quick sort algorithm."""


def quick_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    if len(seq) > 1:
        _quick_sort(seq, 0, len(seq))


def _quick_sort(seq, left, right):
    if left < right:
        middle = _partition(seq, left, right)
        _quick_sort(seq, left, middle - 1)
        _quick_sort(seq, middle + 1, right)


def _partition(seq, left, right):
    pivot = seq[left]
    less = left
    for more in range(less + 1, right):
        if seq[more] <= pivot:
            less += 1
            seq[more], seq[less] = seq[less], seq[more]
    seq[left], seq[less] = seq[less], seq[left]
    return less
