import pytest

import pretty_tables


@pytest.fixture()
def headers():
    return [
        "ID",
        "Name",
        "Occupation",
        "Employed",
    ]


@pytest.fixture()
def rows():
    return [
        [1, "Justin", "Software Engineer", True],
        [2, "Misty", "Receptionist", False],
        [3, "John", None, False],
    ]


@pytest.fixture()
def colors():
    return [
        pretty_tables.Colors.blue,
        pretty_tables.Colors.purple,
        pretty_tables.Colors.bold,
        pretty_tables.Colors.green,
    ]


@pytest.fixture()
def colors_partial():
    """Test a None value inbetween and a missing 4th value"""
    return [
        pretty_tables.Colors.blue,
        pretty_tables.Colors.none,
        pretty_tables.Colors.purple,
    ]
