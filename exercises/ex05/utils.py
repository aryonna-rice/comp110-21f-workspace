"""List utility functions part 2."""

__author__ = "123456789"


# only_evens definition
def only_evens(llist: list[int]) -> list[int]:
    """Given a list of integers, will return the list containing only even numbers."""
    result: list[int] = []
    i: int = 0
    while i < len(llist):
        if (llist[i] % 2) == 0:
            result.append(llist[i])
            i += 1 
        else:
            i += 1
    return result


# sub definition
def sub(llist: list[int], start: int, end: int) -> list[int]:
    """Given a list of integers, a start and stop value, will return the numbers in between."""
    result: list[int] = []
    if start < 0:
        start = 0
    if end > len(llist):
        end = (len(llist))
    if len(llist) == 0 or start > len(llist) or end <= 0:
        return result
    else:
        while start < end:
            result.append(llist[start])
            start += 1
    return result


def concat(lhl: list[int], rhl: list[int]) -> list[int]:
    """Given two lists of integers, will return the two lists as one."""
    result: list[int] = []
    i: int = 0 
    j: int = 0 
    while i < len(lhl):
        result.append(lhl[i])
        i += 1
    while j < len(rhl):
        result.append(rhl[j])
        j += 1
    return result
