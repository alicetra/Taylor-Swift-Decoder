import pytest
from ordered_subset import locate_ordered_lyric_subsets

def test_locate_ordered_lyric_subsets_indices_match():
    small = ['h', 'e', 'l', 'l', 'o']
    large = [['h'], ['e'], ['l'], ['l'], ['o'], ['w'], ['o'], ['r'], ['l'], ['d']]
    expected_output = [[0, 5]]
    assert locate_ordered_lyric_subsets(small, large) == expected_output

def test_locate_ordered_lyric_subsets_no_matches():
    small = ['n', 'o', 'm', 'a', 't', 'c', 'h']
    large = [['h'], ['e'], ['l'], ['l'], ['o'], ['w'], ['o'], ['r'], ['l'], ['d']]
    expected_output = False
    assert locate_ordered_lyric_subsets(small, large) == expected_output

def test_locate_ordered_lyric_subsets_no_match_due_to_order():
    small = ['e', 'h', 'l', 'l', 'o']
    large = [['h'], ['e'], ['l'], ['l'], ['o'], ['w'], ['o'], ['r'], ['l'], ['d']]
    expected_output = False
    assert locate_ordered_lyric_subsets(small, large) == expected_output

def test_locate_ordered_lyric_subsets_middle_match():
    small = ['o', 'r', 'l']
    large = [['h'], ['e'], ['l'], ['l'], ['o'], ['w'], ['o'], ['r'], ['l'], ['d']]
    expected_output = [[6, 9]]
    assert locate_ordered_lyric_subsets(small, large) == expected_output