"""Practice with dictionaries."""

__author__ = "730403391"


def invert(dictonary: dict[str, str]) -> dict[str, str]:
    result_dict: dict[str, str] = {}
    for keys in dictonary:
        value = dictonary[keys]
        if value in result_dict:
            raise KeyError
        else:
            result_dict[value] = keys
    return result_dict


def favorite_color(dictonary: dict[str, str]) -> str:
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
    result: dict[str, int] = {}
    for char in llist:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
