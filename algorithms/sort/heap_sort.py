"""Heap sort algorithm in place."""


def heap_sort(seq):
    _build_max_heep(seq)

    max_index = 0
    heep_size = len(seq) - 1
    for _ in range(heep_size, -1, -1):
        seq[heep_size], seq[max_index] = seq[max_index], seq[heep_size]
        _sift_down(seq, heep_size,  max_index)
        heep_size -= 1



def _build_max_heep(seq):
    """Take a list of elements and sorts them in ascending order.
    
    Args:
        seq: indexed collection
    """
    length = len(seq)
    half = length // 2
    zero = -1

    for index in range(half, zero, -1):
        _sift_down(seq, length, index)


def _sift_down(heap, heep_size,  index):
    while _left_children(index) < heep_size:

        max_index = _left_children(index)
        if _right_children(index) < heep_size and heap[_right_children(index)] > heap[max_index]:
            max_index = _right_children(index)
        
        if heap[index] >= heap[max_index]:
            break

        heap[index], heap[max_index] = heap[max_index], heap[index]
        index = max_index


def _left_children(index):
    return 2 * index + 1


def _right_children(index):
    return 2 * index + 2 
