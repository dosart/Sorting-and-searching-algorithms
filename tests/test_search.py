"""Tests of linear search algorithm."""

import pytest

from algorithms.search import linear_search
from algorithms.search import binary_search


@pytest.mark.parametrize("function", [linear_search, binary_search])
def test_negative_one(function):
    items = [1,2,3,4,5]
    assert(function(items, 6) == -1)


@pytest.mark.parametrize("function", [linear_search, binary_search])
def test_negative_two(function):
    assert(function([], 6) == -1)


@pytest.mark.parametrize("function", [linear_search, binary_search])
def test_positive_one(function):
    items = [1,1,2,3,4]
    assert(function(items, 1) == 0)


@pytest.mark.parametrize("function", [linear_search, binary_search])
def test_positive_two(function):
    items = [1,1,2,3,4]
        
    assert(function(items, 4) == 4)


@pytest.mark.parametrize("function", [linear_search, binary_search])
def test_positive_three(function):
    items = [1,1,2,3,4]
        
    assert(function(items, 2) == 2)
