"""counting sort algorithm."""


def counting_sort(seq):
    """Take list of integer and sort it.

    Args:
        seq: list of integer

    Returns:
        sorted_seq: sorted list
    """
    counts = [0 for _ in range(max(seq) + 1)]

    for element in seq:
        counts[element] += 1

    for index in range(1, len(counts)):
        counts[index] = counts[index] + counts[index - 1]

    sorted_seq = [0 for _ in range(len(seq))]
    for element in seq:
        index = counts[element] - 1
        sorted_seq[index] = element
        counts[element] -= 1

    return sorted_seq
