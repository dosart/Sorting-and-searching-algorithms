"""Tests of 'find_if' algorithm."""

import pytest

from algorithms.search import find_if


class TestFindIfAlgorithm:

    def test_negative_one(self):
        items = [1,2,3,4,5]
        
        assert(find_if(items, lambda x: x > 10) == -1)
    

    def test_negative_two(self):
        assert(find_if([], lambda x: x > 10) == -1)
    

    def test_positive_one(self):
        items = [1,2,3,4,5,6]

        assert(find_if(items, lambda x: x % 2 == 0) == 1)