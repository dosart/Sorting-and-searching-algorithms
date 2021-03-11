"""Tests of counting sort algorithms."""

from  algorithms.sort.counting_sort import counting_sort


def test_list_is_empty():
    items = []
    assert counting_sort(items) == items


def test_list_length_is_one():
    items = [1]
    assert counting_sort(items) == items


def test_list_is_sorted():
    items = [1,1,1,2,2,2,3,4,5]
    assert counting_sort(items) == items


def test_positive_one():
    items = [1,0,2,5,2,1,4,3,2,1,1,3,2]
    assert sorted(items) == counting_sort(items)


def test_positive_two():
    items = [2,1,145,2,9,0,12,4,4,2,1,997,222]
    assert sorted(items) == counting_sort(items)
