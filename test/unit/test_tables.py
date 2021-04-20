import mock
import pytest
from pretty_tables import PrettyTables

TABLE = None
HEADERS = ['ID', 'Name', 'Occupation', 'Employed']
ROWS = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]


def test_generate_table():
    pretty_table = PrettyTables.generate_table(HEADERS, ROWS)
    assert pretty_table == """| ID | Name   | Occupation        | Employed |
| -- | ------ | ----------------- | -------- |
| 1  | Justin | Software Engineer | True     |
| 2  | Misty  | Receptionist      | False    |
| 3  | John   | None              | False    |"""


def test_generate_table_empty_placeholder_value():
    pretty_table = PrettyTables.generate_table(HEADERS, ROWS, 'No data')
    assert pretty_table == """| ID | Name   | Occupation        | Employed |
| -- | ------ | ----------------- | -------- |
| 1  | Justin | Software Engineer | True     |
| 2  | Misty  | Receptionist      | False    |
| 3  | John   | No data           | False    |"""


def test_validate_table_input_no_headers():
    HEADERS = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)


def test_validate_table_input_bad_headers():
    HEADERS = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)


def test_validate_table_input_no_rows():
    ROWS = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)


def test_validate_table_input_bad_rows():
    ROWS = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)


def test_validate_table_input_bad_row_in_rows():
    HEADERS = ['column1']
    ROWS = [
        '123',
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)


def test_validate_table_input_mismatching_column_length():
    HEADERS = ['column1', 'column2']
    ROWS = [
        ['123']
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(HEADERS, ROWS)
