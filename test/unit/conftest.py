import pytest

import pretty_tables


@pytest.fixture(scope='function')
def headers():
    headers = ['ID', 'Name', 'Occupation', 'Employed']

    return headers


@pytest.fixture(scope='function')
def rows():
    rows = [
        [1, 'Justin', 'Software Engineer', True],
        [2, 'Misty', 'Receptionist', False],
        [3, 'John', None, False],
    ]

    return rows


@pytest.fixture(scope='function')
def colors():
    colors = [
        pretty_tables.Colors.blue,
        pretty_tables.Colors.purple,
        pretty_tables.Colors.bold,
        pretty_tables.Colors.green,
    ]

    return colors
