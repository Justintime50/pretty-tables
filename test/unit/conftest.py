"""Fixtures for PrettyTable testing"""
import pytest

from pretty_tables import TableColors


@pytest.fixture(scope='function')
def headers():
    return ['ID', 'Name', 'Occupation', 'Employed']


@pytest.fixture(scope='function')
def rows():
    return [
        [1, 'Justin', 'Software Engineer', True],
        [2, 'Misty', 'Receptionist', False],
        [3, 'John', None, False],
    ]


@pytest.fixture(scope='function')
def colors():
    return [TableColors.OKBLUE, TableColors.HEADER, TableColors.BOLD, TableColors.OKGREEN]
