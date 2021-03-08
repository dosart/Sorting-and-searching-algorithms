"""Heap sort algorithm in place."""

<<<<<<< HEAD

from algorithms.swap import swap

=======
>>>>>>> 01f1c70dd0feb5aaea3b6d23ba4265be0bb4c88e

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
<<<<<<< HEAD
    _build_max_heep(seq)

    max_id = 0
    heep_size = len(seq) - 1
    for _ in range(heep_size, -1, -1):
        swap(seq, heep_size, max_id)
        _sift_down(seq, heep_size, max_id)
        heep_size -= 1


def _build_max_heep(seq):
=======
>>>>>>> 01f1c70dd0feb5aaea3b6d23ba4265be0bb4c88e
    length = len(seq)
    half = length // 2
    zero = -1

    for index in range(half, zero, -1):
        _sift_down(seq, length, index)


<<<<<<< HEAD
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
=======
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
>>>>>>> 01f1c70dd0feb5aaea3b6d23ba4265be0bb4c88e
