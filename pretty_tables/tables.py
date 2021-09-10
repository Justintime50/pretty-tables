class TableColors:
    """A class to contain constants for colors for the table."""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PrettyTables(object):
    """A class used to generate pretty tables for console output."""

    @classmethod
    def generate_table(cls, headers, rows, empty_cell_placeholder=None, colors=None, truthy=None):
        """Generate pretty tables with headers and rows (arrays).

        We do this by validating the headers and rows are valid arrays
        and are set, then convert all items to strings and append
        them to their respective row, then append each row to the table.
        We replace empty items with a placeholder and finally return
        the validated, generated, formatted table.

        Args:
            headers (list): a list of headers for the table.
            rows (list[list]): A list of rows for the table.
            empty_cell_placeholder: The value to be placed in cells with no data.
            colors (list): A list of TableColors for each row.
            truthy (int): Index of the column to be compared for truthy values. If truthy is not None
                truth comparison will override all other formats.
        """
        PrettyTables._validate_table_input(headers, rows)
        table = [headers]
        for row in rows:
            formatted_row = []
            for item in row:
                if item is None:
                    item = empty_cell_placeholder
                formatted_row.append(item)
            table.append(formatted_row)
        formatted_table = cls._format_table(table, colors, truthy)
        return formatted_table

    @staticmethod
    def _format_table(table, colors=None, truthy=None):
        """Take table data and format it into a pretty table.

        This includes adding lines for columns and uniform spacing.

        Args:
            table: The list defining the table to be formatted.
            colors (list): A list of TableColors for each row. If truthy is set to True, colors should
                be set to None, or a list of colors length 2, where the first color is to be used for
                true values and the second color is to be used for false values.
            truthy (int): Index of the column to be compared for truthy values. If truthy is not None
                truth comparison will override all other formats.
        """
        complete_table = []
        col_widths = [max(len(str(item)) for item in column) for column in zip(*table)]
        for line_no, line in enumerate(table):
            if line == table[1]:
                # Add horizontal separator between headers and rows
                complete_table.append(
                    '| '
                    + ' | '.join('{:{}}'.format('-' * col_widths[i], col_widths[i]) for i, item in enumerate(line))
                    + ' |'
                )
            # Check for truthyness and colors.
            if colors or truthy:
                # Check if truthy
                if truthy:
                    # Check has the right number of colors for truthy coloring.
                    if colors and (len(colors) != 0 and len(colors) != 2):
                        raise ValueError(
                            'When using the truthy option you must either specify two colors, or no colors'
                        )
                    # Check the truthy column exist.
                    if not isinstance(truthy, int) or not 0 < truthy < len(line):
                        raise ValueError(f'The column specified for truthy values does not exist. Column {truthy}')
                    # Default truthy colors if no colors are specified.
                    if not colors or len(colors) == 0:
                        colors = [TableColors.OKGREEN, TableColors.FAIL]
                    complete_table.append(
                        '| '
                        + ' | '.join(
                            f'{"" if line_no == 0 else colors[0] if bool(line[truthy]) else colors[1]}'
                            f'{str(item):{col_widths[i]}}{TableColors.ENDC}'
                            for i, item in enumerate(line)
                        )
                        + ' |'
                    )
                else:
                    # Set colors.
                    complete_table.append(
                        '| '
                        + ' | '.join(
                            f'{colors[i]}{str(item):{col_widths[i]}}{TableColors.ENDC}' for i, item in enumerate(line)
                        )
                        + ' |'
                    )
            else:
                complete_table.append(
                    '| ' + ' | '.join('{:{}}'.format(str(item), col_widths[i]) for i, item in enumerate(line)) + ' |'
                )

        formatted_table = '\n'.join(complete_table)
        return formatted_table

    @staticmethod
    def _validate_table_input(headers, rows, colors=None):
        """Validate table input.

        Checking that headers and rows are set and each are a
        valid list and correct length.

        Args:
            headers (list): A list of headers for the table.
            rows (list): A list of lists matching the length of headers for each row.
            colors (list): A list of TableColors for each column.
        """
        if not headers or not isinstance(headers, list):
            raise ValueError('Headers are either not set or are not a proper array.')
        elif not rows or not isinstance(rows, list):
            raise ValueError('Rows are either not set or are not a proper array.')
        if colors:
            if not isinstance(colors, list):
                raise ValueError('Colors are set but are not a proper array.')
            elif len(colors) != len(headers):
                raise IndexError('The number of colors does not match the number of columns.')
        table_length = len(headers)
        for i, row in enumerate(rows):
            if not isinstance(row, list):
                raise IndexError(f'Row {i + 1} is not a proper array.')
            row_length = len(row)
            if row_length != table_length:
                raise IndexError(
                    f'Row {i + 1} has {row_length} column(s) which does not match the table columns of {table_length}.'
                )

        return True
