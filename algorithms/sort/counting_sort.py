
"""Counting sort algorithm."""


def counting_sort(seq):
    """Take a list of integer and sorted it.

    Args:
        seq (list of integer): source data

    Returns:
        sorted_seq (list of integer) sorted collection
    """
    if len(seq) > 1:
        return _counting_sort(seq)
    return seq


def _counting_sort(seq):
    counts = [0 for _ in range(max(seq) + 1)]

    for element in seq:
        counts[element] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]

    sorted_seq = [0 for _ in range(len(seq))]
    for element in seq:
        counts[element] -= 1
        sorted_seq[counts[element]] = element

    return sorted_seq
