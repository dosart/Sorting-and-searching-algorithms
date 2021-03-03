"""Tests of sort algorithms."""

import pytest

from algorithms.sort.bubble_sort import bubble_sort


@pytest.mark.parametrize("function", [bubble_sort])
def test_positive_zero(function):
    items = []

    function(items)

    assert(items == [])


@pytest.mark.parametrize("function", [bubble_sort])
def test_positive_one(function):
    items = [-1,0,2,3,4,6,7,4,0]

    function(items)

    assert(items == [-1,0,0,2,3,4,4,6,7])


@pytest.mark.parametrize("function", [bubble_sort])
def test_positive_two(function):
    items = [1,1,1,1]

    function(items)

    assert(items == [1,1,1,1])
