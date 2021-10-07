"""Practice with dictionaries."""

__author__ = "730403391"


def invert(dictonary: dict[str, str]) -> dict[str, str]:
    """Takes the keys of one dictionary and makes them the values of another. Swaps key and values."""
    result_dict: dict[str, str] = {}
    for keys in dictonary:
        value = dictonary[keys]
        if value in result_dict:
            raise KeyError("Same keys detected.")
        else:
            result_dict[value] = keys
    return result_dict


def favorite_color(dictonary: dict[str, str]) -> str:
    """Returns the most frequent color."""
    count_dict: dict[str, int] = {}
    for keys in dictonary:
        if dictonary[keys] in count_dict:
            count_dict[dictonary[keys]] += 1
        else:
            count_dict[dictonary[keys]] = 1
    dummy: int = 0
    winning_color: str = ""
    for color in count_dict:
        if count_dict[color] > dummy:
            dummy = count_dict[color]
            winning_color = color
    return winning_color


def count(llist: list[str]) -> dict[str, int]:
    """Creates a dictionary of the number of times a character appears within a list of strings."""
    result: dict[str, int] = {}
    for char in llist:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
