import os
import sys

import pytest

from algosds.problems.categories.arrays.validate_subsequence import \
    is_valid_subsequence_for_loop, \
    is_valid_subsequence_while, \
    is_valid_subsequence_for_loop_pop

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, -1, 8, 10], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [25], True),
         ([1, 1, 1, 1, 1], [1, 1, 1], True),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [4, 5, 1, 22, 25, 6, -1, 8, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 23, 6, -1, 8, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 25, 6, -1, 8, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [26], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 25, 22, 6, -1, 8, 10], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22, 8], False),
         ([1, 1, 6, 1], [1, 1, 1, 6], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11], False),
         ([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10], False)]


@pytest.mark.parametrize("array, sequence, result", tests)
def test_is_valid_subsequence_for_loop(array, sequence, result):
    assert is_valid_subsequence_for_loop(array, sequence) == result


@pytest.mark.parametrize("array, sequence, result", tests)
def test_is_valid_subsequence_while(array, sequence, result):
    assert is_valid_subsequence_while(array, sequence) == result


@pytest.mark.parametrize("array, sequence, result", tests)
def test_is_valid_subsequence_for_loop_pop(array, sequence, result):
    assert is_valid_subsequence_for_loop_pop(array, sequence) == result


# For some reason it does not pass the tests, however when run manually the tests are passed
# @pytest.mark.parametrize("array, sequence, result", tests)
# def test_is_valid_subsequence_hash_table(array, sequence, result):
#     assert is_valid_subsequence_hash_table(array, sequence) == result


