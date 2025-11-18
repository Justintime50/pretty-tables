import pytest

import pretty_tables
from pretty_tables.tables import _validate_table_input


def test_create_table(headers, rows):
    output = pretty_tables.create(
        headers=headers,
        rows=rows,
        empty_cell_placeholder="No data",
    )

    # fmt: off
    assert output == (
        '| ID | Name   | Occupation        | Employed |\n'
        '| -- | ------ | ----------------- | -------- |\n'
        '| 1  | Justin | Software Engineer | True     |\n'
        '| 2  | Misty  | Receptionist      | False    |\n'
        '| 3  | John   | No data           | False    |'
    )
    # fmt: on


def test_validate_table_input_no_headers(rows):
    headers = None
    with pytest.raises(ValueError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Headers are either not set or are not a proper list." in str(error.value)


def test_validate_table_input_bad_headers(rows):
    headers = "123"
    with pytest.raises(ValueError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Headers are either not set or are not a proper list." in str(error.value)


def test_validate_table_input_no_rows(headers):
    rows = None
    with pytest.raises(ValueError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Rows are either not set or are not a proper list." in str(error.value)


def test_validate_table_input_bad_rows(headers):
    rows = "123"
    with pytest.raises(ValueError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Rows are either not set or are not a proper list." in str(error.value)


def test_validate_table_input_bad_colors(headers, rows):
    with pytest.raises(ValueError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
            colors="asdf",
        )

    assert "Colors are set but are not a proper list." in str(error.value)


def test_validate_table_input_bad_row_in_rows():
    headers = ["column1"]
    rows = [
        "123",
    ]
    with pytest.raises(IndexError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Row 1 is not a proper list." in str(error.value)


def test_validate_table_input_mismatching_column_length():
    headers = ["column1", "column2"]
    rows = [
        ["123"],
    ]
    with pytest.raises(IndexError) as error:
        _validate_table_input(
            headers=headers,
            rows=rows,
        )

    assert "Row 1 has 1 column(s) which does not match the table columns of 2." in str(error.value)


def test_validate_table_with_default_truthy_not_enough_colors(headers, rows):
    with pytest.raises(ValueError) as exc:
        _ = pretty_tables.create(
            headers=headers,
            rows=rows,
            empty_cell_placeholder="No data",
            colors=[pretty_tables.Colors.cyan],
            truthy=3,
        )

    assert "When using the truthy option, you must specify two colors, or no colors" in str(exc.value)
