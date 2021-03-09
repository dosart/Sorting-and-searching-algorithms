"""Heap sort algorithm in place."""


from algorithms.swap import swap


def heap_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    _build_max_heap(seq)

    max_id = 0
    heap_size = len(seq) - 1
    while heap_size >= 0:
        swap(seq, max_id, heap_size)
        _sift_down(seq, heap_size, max_id)
        heap_size -= 1


def _build_max_heap(seq):
    length = len(seq)
    half = length // 2
    zero = -1

    for index in range(half, zero, -1):
        _sift_down(seq, length, index)


def _sift_down(heap, heap_size, index):
    while _left_children(index) < heap_size:

        right = _right_children(index)
        left = _left_children(index)
        max_id = left

        if right < heap_size and heap[right] > heap[max_id]:
            max_id = right

        if heap[index] >= heap[max_id]:
            break

        swap(heap, index, max_id)
        index = max_id


def _left_children(index):
    return 2 * index + 1


def _right_children(index):
    return 2 * index + 2
