import pytest
import mock
from pretty_tables import PrettyTables


def test_generate_table(headers, rows):
    pretty_table = PrettyTables.generate_table(headers, rows, 'No data')
    assert pretty_table == """| ID | Name   | Occupation        | Employed |
| 1  | Justin | Software Engineer | True     |
| 2  | Misty  | Receptionist      | False    |
| 3  | John   | No data           | False    |"""


def test_validate_table_input_no_headers(rows):
    headers = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)


def test_validate_table_input_bad_headers(rows):
    headers = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)


def test_validate_table_input_no_rows(headers):
    rows = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)


def test_validate_table_input_bad_rows(headers):
    rows = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)


def test_validate_table_input_bad_row_in_rows():
    headers = ['column1']
    rows = [
        '123',
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(headers, rows)


def test_validate_table_input_mismatching_column_length():
    headers = ['column1', 'column2']
    rows = [
        ['123']
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(headers, rows)
