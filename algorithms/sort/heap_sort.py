"""Heap sort algorithm in place."""


from algorithms.swap import swap


def heap_sort(seq):
    """Take a list of elements and sorts them in ascending order.

    Args:
        seq: indexed collection
    """
    _build_max_heep(seq)

    max_id = 0
    heep_size = len(seq) - 1
    for _ in range(heep_size, -1, -1):
        swap(seq, heep_size, max_id)
        _sift_down(seq, heep_size, max_id)
        heep_size -= 1


def _build_max_heep(seq):
    length = len(seq)
    half = length // 2
    zero = -1

    for index in range(half, zero, -1):
        _sift_down(seq, length, index)


def _sift_down(heap, heep_size, index):
    while _left_child(index) < heep_size:

        left = _left_child(index)
        right = _right_child(index)
        max_id = left

        if right < heep_size and heap[right] > heap[max_id]:
            max_id = right

        if heap[index] >= heap[max_id]:
            break

        swap(heap, index, max_id)
        index = max_id


def _left_child(index):
    return 2 * index + 1


def _right_child(index):
    return 2 * index + 2
