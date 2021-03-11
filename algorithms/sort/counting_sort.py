
"""Counting sort algorithm."""


def counting_sort(seq):
    """Take a list of integer and sorted it.
    
    Args:
        seq (list of integer) source data
    
    Returns:
        sorted_seq (list of integer) sorted collection
    """
    if len(seq) > 1:
        return _counting_sort(seq)
    else:
        return seq


def _counting_sort(seq):
    counts = [0] * (max(seq) + 1)

    for element in seq:
        counts[element] = counts[element] + 1

    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]

    sorted_seq = [0] * len(seq)
    for element in seq:
        position = counts[element] - 1
        counts[element] = counts[element] - 1
        sorted_seq[position] = element

    return sorted_seq
