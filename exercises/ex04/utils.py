"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def all(llist: list[int], number: int) -> bool:
    x: bool = True
    i: int = 0 
    if len(llist) == 0:
        x = False
        return x
    while i < len(llist):
        if llist[i] == number:
            i += 1
        x = False
        return x
    return x


def is_equal(leflist: list[int], rightlist: list[int]) -> bool:
    i: int = 0 
    x: bool = True
    while i < len(leflist):
        if len(leflist) != len(rightlist):
            raise AssertionError
        if leflist[i] == rightlist[i]:
            i += 1
        x = False
        return x
    return x


def max(llist: list[int]) -> int:
    i: int = 0
    start: int = llist[0]
    while i < len(llist):
        if start < llist[i]:
            start = llist[i]
        i += 1
    return start


test: bool = is_equal([1, 2, 4], [1, 2, 3])
print(test)

print(max([40, 9000, 40, 60]))