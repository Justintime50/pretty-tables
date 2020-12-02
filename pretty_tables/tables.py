"""The tables module for the pretty_tables library."""


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

    @staticmethod
    def generate_table(headers, rows, empty_cell_placeholder=None, colors=None):
        """
        Generate pretty tables with headers and rows (arrays).

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
        """
        PrettyTables._validate_table_input(headers, rows)
        table = [headers]
        for row in rows:
            formatted_row = []
            for item in row:
                if item is True:
                    data = 'True'
                elif item is False:
                    data = 'False'
                elif item:
                    data = item
                else:
                    data = empty_cell_placeholder
                formatted_row.append(str(data))
            table.append(formatted_row)
        formatted_table = PrettyTables._format_table(table, colors)
        return formatted_table

    @staticmethod
    def _format_table(table, colors=None):
        """
        Take table data and format it into a pretty table.

        This includes adding lines for columns and uniform spacing.

        Args:
            table: The list defining the table to be formatted.
            colors (list): A list of TableColors for each row.
        """
        complete_table = []
        col_widths = [max(len(str(item)) for item in column) for column in zip(*table)]
        for line in table:
            if colors:
                complete_table.append('| ' + ' | '.join(f'{colors[i]}{item:{col_widths[i]}}{TableColors.ENDC}'
                                                        for i, item in enumerate(line)) + ' |')
            else:
                complete_table.append('| ' + ' | '.join('{:{}}'.format(item, col_widths[i])
                                                        for i, item in enumerate(line)) + ' |')

        formatted_table = '\n'.join(complete_table)
        return formatted_table

    @staticmethod
    def _validate_table_input(headers, rows, colors=None):
        """
        Validate table input.

        Checking that headers and rows are set and each are a
        valid list and correct length.

        Args:
            headers (list): A list of headers for the table.
            rows (list): A list of lists matching the length of headers for each row.
            colors (list): A list of TableColors for each column.
        """
        if not headers or not isinstance(headers, list):
            raise ValueError(
                'Headers are either not set or are not a proper array.'
            )
        elif not rows or not isinstance(rows, list):
            raise ValueError(
                'Rows are either not set or are not a proper array.'
            )
        if colors:
            if not isinstance(colors, list):
                raise ValueError(
                    'Colors are set but are not a proper array.'
                )
            elif len(colors) != len(headers):
                raise IndexError('The number of colors does not mach the number of columns.')
        table_length = len(headers)
        for i, row in enumerate(rows):
            if not isinstance(row, list):
                raise IndexError(
                    f'Row {i + 1} is not a proper array.'
                )
            row_length = len(row)
            if row_length != table_length:
                raise IndexError(
                    f'Row {i + 1} has {row_length} column(s) which does not match the table columns of {table_length}.'
                )

        return True
