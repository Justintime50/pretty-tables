import pytest
import mock
from pretty_tables import PrettyTables


def test_generate_table(headers, rows):
    pretty_table = PrettyTables.generate_table(headers, rows, 'No data')
    assert pretty_table == "| ID | Name   | Occupation        | Employed |\n" \
                           "| 1  | Justin | Software Engineer | True     |\n" \
                           "| 2  | Misty  | Receptionist      | False    |\n" \
                           "| 3  | John   | No data           | False    |"


def test_generate_table_with_colors(headers, rows, colors):
    pretty_table = PrettyTables.generate_table(headers, rows, 'No data', colors)
    assert pretty_table == \
           '| \x1b[94mID\x1b[0m | \x1b[95mName  \x1b[0m | \x1b[1mOccupation       \x1b[0m ' \
           '| \x1b[92mEmployed\x1b[0m |\n' \
           '| \x1b[94m1 \x1b[0m | \x1b[95mJustin\x1b[0m | \x1b[1mSoftware Engineer\x1b[0m ' \
           '| \x1b[92mTrue    \x1b[0m |\n' \
           '| \x1b[94m2 \x1b[0m | \x1b[95mMisty \x1b[0m | \x1b[1mReceptionist     \x1b[0m ' \
           '| \x1b[92mFalse   \x1b[0m |\n' \
           '| \x1b[94m3 \x1b[0m | \x1b[95mJohn  \x1b[0m | \x1b[1mNo data          \x1b[0m ' \
           '| \x1b[92mFalse   \x1b[0m |'


def test_validate_table_input_no_headers(rows):
    headers = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Headers are either not set or are not a proper array.' in str(error.value)


def test_validate_table_input_bad_headers(rows):
    headers = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Headers are either not set or are not a proper array.' in str(error.value)


def test_validate_table_input_no_rows(headers):
    rows = None
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Rows are either not set or are not a proper array.' in str(error.value)


def test_validate_table_input_bad_rows(headers):
    rows = '123'
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Rows are either not set or are not a proper array.' in str(error.value)


def test_validate_table_input_bad_colors(headers, rows):
    with pytest.raises(ValueError) as error:
        PrettyTables._validate_table_input(headers, rows, colors='asdf')
    assert 'Colors are set but are not a proper array.' in str(error.value)


def test_validate_table_input_colors_bad_length(headers, rows):
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(headers, rows, colors=[1, 2])
    assert 'The number of colors does not mach the number of columns.' in str(error.value)


def test_validate_table_input_bad_row_in_rows():
    headers = ['column1']
    rows = [
        '123',
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Row 1 is not a proper array.' in str(error.value)


def test_validate_table_input_mismatching_column_length():
    headers = ['column1', 'column2']
    rows = [
        ['123']
    ]
    with pytest.raises(IndexError) as error:
        PrettyTables._validate_table_input(headers, rows)
    assert 'Row 1 has 1 column(s) which does not match the table columns of 2.' in str(error.value)
