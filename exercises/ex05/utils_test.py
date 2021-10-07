"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"


from exercises.ex05.utils import only_evens, sub, concat


# only_evens tests
def test_only_evens_odds() -> None:
    assert only_evens([1, 5, 7, 9]) == []


def test_only_evens_evens() -> None:
    assert only_evens([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]


def test_only_evens_blank() -> None:
    assert only_evens([]) == []


# sub tests:

def test_sub_reg() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_end_too_big() -> None:
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 18) == [2, 3, 4, 5, 6, 7, 8, 9]


def concat_works() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == ([1, 2, 3, 4, 5, 6])
