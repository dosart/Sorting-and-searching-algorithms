"""Tests of linear search algorithm."""

import pytest

from algorithms.search import linear_search


class TestLinearSearchAlgorithm:
    
    def test_negative(self):
        l = [1,2,3,4,5]
        
        assert(linear_search(l, 6) == -1)

