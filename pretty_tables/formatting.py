from typing import (
    Any,
    List,
    Optional,
)


class Colors:
    """A collection of colors and formatters you can use to customize
    the output of your pretty table.
    """

    # Colors
    black = "\033[90m"
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    purple = "\033[95m"
    red = "\033[91m"
    white = "\033[97m"
    yellow = "\033[93m"

    # Formatting
    bold = "\033[1m"
    reset = "\033[0m"  # Resets all text formatting
    underline = "\033[4m"
    none = "\033[0m"  # Same as `reset`


def _format_table(table: List[Any], colors: Optional[List[Colors]] = None, truthy: Optional[int] = None) -> str:
    """Take table data and format it into a pretty table.

    This includes adding lines for columns and uniform spacing.

    Args:
        - table: The list defining the table to be formatted.
        - colors: A list of Colors for each row. If truthy is set to True, colors should
        be set to None, or a list of colors length 2, where the first color is to be used for
        true values and the second color is to be used for false values.
        - truthy: Index of the column to be compared for truthy values. If truthy is not None
        truth comparison will override all other formats.
    """
    complete_table = []
    table_left_border = "| "
    table_column_divider = " | "
    table_right_boder = " |"
    table_header_divider = "-"
    col_widths = [max(len(str(item)) for item in column) for column in zip(*table)]

    for line_number, line in enumerate(table):
        if line == table[1]:
            # Add horizontal separator between headers and rows
            complete_table.append(
                table_left_border
                + table_column_divider.join(
                    "{:{}}".format(table_header_divider * col_widths[i], col_widths[i]) for i, item in enumerate(line)
                )
                + table_right_boder
            )

        if truthy:
            # Check that the truthy column exists
            valid_truthy_values = isinstance(truthy, int) and 0 < truthy < len(line)
            if not valid_truthy_values:
                raise ValueError(f"The column specified for truthy values does not exist. Column: {truthy}")

            # Use default truthy colors if no colors are specified.
            truthy_color = colors[0] if colors else Colors.green
            non_truthy_color = colors[1] if colors else Colors.red

            # Generate truthy and non-truthy rows
            complete_table.append(
                table_left_border
                + table_column_divider.join(
                    f'{"" if line_number == 0 else truthy_color if bool(line[truthy]) else non_truthy_color}'
                    f"{str(item):{col_widths[i]}}{Colors.reset}"
                    for i, item in enumerate(line)
                )
                + table_right_boder
            )
        elif not truthy and colors is not None:
            # Set custom colors
            complete_table.append(
                table_left_border
                + table_column_divider.join(
                    f"{colors[i] if len(colors) > i else Colors.none}{str(item):{col_widths[i]}}{Colors.reset}"
                    for i, item in enumerate(line)
                )
                + table_right_boder
            )
        else:
            # No custom variables set, generate vanilla table
            complete_table.append(
                table_left_border
                + table_column_divider.join("{:{}}".format(str(item), col_widths[i]) for i, item in enumerate(line))
                + table_right_boder
            )

    formatted_table = "\n".join(complete_table)

    return formatted_table
