"""Merge sort algorithm."""


def merge_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    if len(seq) > 1:
        _merge_sort(seq, 0, len(seq) - 1)


def _merge_sort(seq, left, right):
    if left < right:
        middle = (left + right) // 2
        _merge_sort(seq, left, middle)
        _merge_sort(seq, middle + 1, right)
        _merge(seq, left, middle, right)


def _merge(seq, left, middle, right):
    tmps = []
    for tmp in seq:
        tmps.append(tmp)

    left_cursor = left
    right_cursor = middle + 1
    seq_cursor = left

    while left_cursor <= middle and right_cursor <= right:
        if tmps[left_cursor] < tmps[right_cursor]:
            seq[seq_cursor] = tmps[left_cursor]
            left_cursor += 1
            seq_cursor += 1
        else:
            seq[seq_cursor] = tmps[right_cursor]
            right_cursor += 1
            seq_cursor += 1

    while left_cursor <= middle:
        seq[seq_cursor] = tmps[left_cursor]
        left_cursor += 1
        seq_cursor += 1

    while right_cursor <= right:
        seq[seq_cursor] = tmps[right_cursor]
        right_cursor += 1
        seq_cursor += 1
