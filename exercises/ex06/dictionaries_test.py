"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"

from exercises.ex06.dictionaries import invert, favorite_color, count


def test_a() -> None:
    """Invert."""
    assert invert({}) == {}


def test_b() -> None:
    """Invert."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_c() -> None:
    """Invert."""
    assert invert({'Aryonna': 'Rice', 'Jerry': 'Rice'}) == KeyError


def test_d() -> None:
    """Test count."""
    assert count(["A", "a"]) == {"A": 1, "a": 1}


def test_e() -> None:
    """Test count."""
    assert count(["a", "b", "c", "a"]) == {"a": 2, "b": 1, "c": 1}


def test_f() -> None:
    """Test count."""
    assert count(["aryonna", "rice"]) == {"aryonna": 1, "rice": 1}


def test_g() -> None:
    """Test fav_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_z() -> None:
    """Test fav_color."""
    assert favorite_color({"Marc": "orange", "Ezri": "blue", "Kris": "blue", "Aryonna": "orange"}) == "orange"


def test_h() -> None:
    """Test fav_color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Me": "yellow"}) == "yellow"