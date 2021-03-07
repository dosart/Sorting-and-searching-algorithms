"""Heap sort algorithm in place."""

import heapq


def heap_sort(seq):
    """Take a list of elements and sorts them in ascending order.
    
    Args:
        seq: indexed collection
    """
    heapq.heapify(seq)