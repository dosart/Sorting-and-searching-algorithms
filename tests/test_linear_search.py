"""Tests of linear search algorithm."""

import pytest

from algorithms.search import linear_search


class TestLinearSearchAlgorithm:
    
    def test_negative_one(self):
        items = [1,2,3,4,5]
        
        assert(linear_search(items, 6) == -1)


    def test_negative_two(self):
        assert(linear_search([], 6) == -1)


    def test_positive_one(self):
        items = [1,1,2,3,4]
        
        assert(linear_search(items, 1) == 0)


    def test_positive_two(self):
        items = [1,1,2,3,4]
        
        assert(linear_search(items, 4) == 4)


    def test_positive_three(self):
        items = [1,1,2,3,4]
        
        assert(linear_search(items, 2) == 2)
