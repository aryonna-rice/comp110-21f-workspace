"""Utility functions."""

__author__ = "730403391"

from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(list_of_rows: list[dict[str, str]], column: str) -> list[str]:
    """Gets a list of column values."""
    result: list[str] = []
    for key in list_of_rows:
        result.append(key[column])
    return result


def columnar(llist: list[dict[str, str]]) -> dict[str, list[str]]:
    """Creates a column oriented table using the coloumn_values function."""
    result_dict: dict[str, list[str]] = {}
    for dictionaries in llist:
        for keys in dictionaries:
            result_dict[keys] = column_values(llist, keys)
    return result_dict


def head(table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Returns a specifed number of rows."""
    result_dict: dict[str, list[str]] = {}
    for key in table:
        first_number_values: list[str] = []
        for i in range(number):
            if number >= len(table[key]):
                return table
            else:
                first_number_values.append(table[key][i])
        result_dict[key] = first_number_values
    return result_dict


def select(dictionary: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary with specified columns."""
    result_dict: dict[str, list[str]] = {}
    for name in names:
        if name in dictionary.keys():
            result_dict[name] = dictionary[name]
    return result_dict


def concat(lhdict: dict[str, list[str]], rhdict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a jumbo dictionary."""
    result_dict: dict[str, list[str]] = {}
    for key in lhdict:
        result_dict[key] = lhdict[key]
    for key in rhdict:
        if key in result_dict:
            i: int = 0
            values: list[str] = []
            while i < len(rhdict[key]):
                values = result_dict[key]
                rh_values: list[str] = rhdict[key]
                values.append(rh_values[i])
                i += 1
            result_dict[key] = values
        else:
            result_dict[key] = rhdict[key]
    return result_dict


def count(llist: list[str]) -> dict[str, int]:
    """Counts the number of occurances."""
    result_dict: dict[str, int] = {}
    for character in llist:
        if character in result_dict:
            result_dict[character] += 1
        else:
            result_dict[character] = 1
    return result_dict