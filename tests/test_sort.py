"""Tests of sort algorithms."""

import pytest

from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.insetrion_sort import insetrion_sort
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.sort.heap_sort import heap_sort


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_list_is_empty(function):
    items = []
    function(items)
    assert(items == [])


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_positive_one(function):
    items = [-1,0,2,3,4,6,7,4,0]
    function(items)
    assert(items == [-1,0,0,2,3,4,4,6,7])


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_even_length(function):
    items = [1,0,4,3]
    function(items)
    assert(items == [0,1,3,4])


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_positive_two(function):
    items = [1,1,1,1]
    function(items)
    assert(items == [1,1,1,1])


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_one_elemtn(function):
    items = [1]
    function(items)
    assert(items == [1])


@pytest.mark.parametrize("function", [bubble_sort, insetrion_sort, merge_sort, quick_sort, heap_sort])
def test_floating_point(function):
    items = [1.1, 1]
    function(items)
    assert(items == [1,1.1])
