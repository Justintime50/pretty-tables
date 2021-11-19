from typing import List, Optional


class Colors:
    """A collection of colors and formatters you can use to customize
    the output of your pretty table.
    """

    # Colors
    black = '\033[90m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    purple = '\033[95m'
    red = '\033[91m'
    white = '\033[97m'
    yellow = '\033[93m'

    # Formatting
    bold = '\033[1m'
    reset = '\033[0m'  # Resets all text formatting
    underline = '\033[4m'


class PrettyTable:
    def __init__(self, headers: List, rows: List[List]):
        self.headers = headers
        self.rows = rows

    def generate(
        self,
        empty_cell_placeholder: Optional[str] = None,
        colors: Optional[List] = None,
        truthy: Optional[List] = None,
    ) -> str:
        """Generate pretty tables with headers and rows.

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
        self._validate_table_input(truthy, colors)
        table = [self.headers]

        for row in self.rows:
            formatted_row = []
            for item in row:
                if item is None:
                    item = empty_cell_placeholder
                formatted_row.append(item)
            table.append(formatted_row)

        formatted_table = self._format_table(table, colors, truthy)

        return formatted_table

    @staticmethod
    def _format_table(table: List, colors: Optional[List] = None, truthy: Optional[int] = None) -> str:
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
        table_left_border = '| '
        table_column_divider = ' | '
        table_right_boder = ' |'
        table_header_divider = '-'
        col_widths = [max(len(str(item)) for item in column) for column in zip(*table)]

        for line_number, line in enumerate(table):
            if line == table[1]:
                # Add horizontal separator between headers and rows
                complete_table.append(
                    table_left_border
                    + table_column_divider.join(
                        '{:{}}'.format(table_header_divider * col_widths[i], col_widths[i])
                        for i, item in enumerate(line)
                    )
                    + table_right_boder
                )

            # Check for truthyness and colors
            if colors or truthy:
                # Check if truthy
                if truthy:
                    # Check if the input has the correct number of colors for truthy coloring
                    valid_num_color_entries = {0, 2}
                    if colors and (len(colors) not in valid_num_color_entries):
                        raise ValueError('When using the truthy option, you must specify two colors, or no colors')

                    # Check that the truthy column exists
                    valid_truthy_values = isinstance(truthy, int) and 0 < truthy < len(line)
                    if not valid_truthy_values:
                        raise ValueError(f'The column specified for truthy values does not exist. Column: {truthy}')

                    # Use default truthy colors if no colors are specified.
                    truthy_color = colors[0] if colors else Colors.green
                    non_truthy_color = colors[1] if colors else Colors.red

                    # Generate truthy and non-truthy rows
                    complete_table.append(
                        table_left_border
                        + table_column_divider.join(
                            f'{"" if line_number == 0 else truthy_color if bool(line[truthy]) else non_truthy_color}'
                            f'{str(item):{col_widths[i]}}{Colors.reset}'
                            for i, item in enumerate(line)
                        )
                        + table_right_boder
                    )
                else:
                    # Set custom colors
                    complete_table.append(
                        table_left_border
                        + table_column_divider.join(
                            f'{colors[i]}{str(item):{col_widths[i]}}{Colors.reset}' for i, item in enumerate(line)
                        )
                        + table_right_boder
                    )
            else:
                # No custom variables set, generate vanilla table
                complete_table.append(
                    table_left_border
                    + table_column_divider.join('{:{}}'.format(str(item), col_widths[i]) for i, item in enumerate(line))
                    + table_right_boder
                )

        formatted_table = '\n'.join(complete_table)

        return formatted_table

    def _validate_table_input(self, truthy: Optional[int] = None, colors: Optional[List] = None):
        """Validate table input checking that headers and rows are set and each are a
        valid list and correct length.

        Args:
            - headers: A list of headers for the table.
            - rows: A list of lists matching the length of headers for each row.
            - colors: A list of Colors for each column.
        """
        if not self.headers or not isinstance(self.headers, list):
            raise ValueError('Headers are either not set or are not a proper list.')
        elif not self.rows or not isinstance(self.rows, list):
            raise ValueError('Rows are either not set or are not a proper list.')
        else:
            # Headers and rows setup correctly, do nothing
            pass

        if colors:
            if not isinstance(colors, list):
                raise ValueError('Colors are set but are not a proper list.')
            elif not truthy and len(colors) != len(self.headers):
                raise IndexError('The number of colors does not match the number of columns.')

        table_length = len(self.headers)
        for i, row in enumerate(self.rows):
            if not isinstance(row, list):
                raise IndexError(f'Row {i + 1} is not a proper list.')
            row_length = len(row)
            if row_length != table_length:
                raise IndexError(
                    f'Row {i + 1} has {row_length} column(s) which does not match the table columns of {table_length}.'
                )
