import pytest
from Applications import Count

def test_count_zeros():
    assert Count.count([0,0,0], 0) == 3

def test_count_string():
    assert Count.count(["a","a","a"], "a") == 3