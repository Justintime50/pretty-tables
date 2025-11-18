from typing import (
    Any,
    List,
    Optional,
)

from pretty_tables.formatting import (
    Colors,
    _format_table,
)


def create(
    headers: List[Any],
    rows: List[List[Any]],
    empty_cell_placeholder: Optional[str] = None,
    colors: Optional[List[Colors]] = None,
    truthy: Optional[int] = None,
) -> str:
    """Create a pretty table with headers and rows.

    We do this by validating the headers and rows are valid lists
    and are set, then convert all items to strings and append
    them to their respective row, then append each row to the table.
    We replace empty items with a placeholder and finally return
    the validated, generated, formatted table.

    Args:
        - headers: a list of headers for the table.
        - rows: A list of rows for the table.
        - empty_cell_placeholder: The value to be placed in cells with no data.
        - colors: A list of Colors for each row.
        - truthy: Index of the column to be compared for truthy values. If truthy is not None
        truth comparison will override all other formats.
    """
    _validate_table_input(headers, rows, truthy, colors)
    table = [headers]

    for row in rows:
        formatted_row = []
        for item in row:
            if item is None:
                item = empty_cell_placeholder
            formatted_row.append(item)
        table.append(formatted_row)

    formatted_table = _format_table(table, colors, truthy)

    return formatted_table


def _validate_table_input(
    headers: List[Any], rows: List[List[Any]], truthy: Optional[int] = None, colors: Optional[List] = None
):
    """Validate table input checking that headers and rows are set and each are a
    valid list and correct length.

    Args:
        - headers: A list of headers for the table.
        - rows: A list of lists matching the length of headers for each row.
        - colors: A list of Colors for each column.
    """
    if not headers or not isinstance(headers, list):
        raise ValueError("Headers are either not set or are not a proper list.")
    elif not rows or not isinstance(rows, list):
        raise ValueError("Rows are either not set or are not a proper list.")
    else:
        # Headers and rows setup correctly, do nothing
        pass

    if colors:
        if not isinstance(colors, list):
            raise ValueError("Colors are set but are not a proper list.")
        if truthy:
            # Check if the input has the correct number of colors for truthy coloring
            valid_num_color_entries = {0, 2}
            if colors and (len(colors) not in valid_num_color_entries):
                raise ValueError("When using the truthy option, you must specify two colors, or no colors")

    table_length = len(headers)
    for i, row in enumerate(rows):
        if not isinstance(row, list):
            raise IndexError(f"Row {i + 1} is not a proper list.")
        row_length = len(row)
        if row_length != table_length:
            raise IndexError(
                f"Row {i + 1} has {row_length} column(s) which does not match the table columns of {table_length}."
            )
