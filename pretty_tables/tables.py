class PrettyTables():
    @classmethod
    def generate_table(cls, headers, rows, empty_cell_placeholder=None):
        """Generate pretty tables with headers and rows (arrays).
        We do this by validating the headers and rows are valid arrays
        and are set, then convert all items to strings and append
        them to their respective row, then append each row to the table.
        We replace empty items with a placeholder and finally return
        the validated, generated, formatted table.

        headers = 1d array
        rows = 2d array
        empty_cell_placeholder = whatever you want in place of an empty cell
        """
        cls._validate_table_input(headers, rows)
        table = []
        table.append(headers)
        for row in rows:
            formatted_row = []
            for item in row:
                if item is None:
                    item = empty_cell_placeholder
                formatted_row.append(str(item))
            table.append(formatted_row)
        formatted_table = cls._format_table(table)
        return formatted_table

    @classmethod
    def _format_table(cls, table):
        """Take table data and format it into a pretty table
        including lines for columns and uniform spacing.
        """
        complete_table = []
        col_widths = [max(len(str(item)) for item in column) for column in zip(*table)]
        for line in table:
            if line == table[1]:
                # Add horizontal separator between headers and rows
                complete_table.append('| ' + ' | '.join('{:{}}'.format('-' * col_widths[i], col_widths[i])
                                                        for i, item in enumerate(line)) + ' |')
            complete_table.append('| ' + ' | '.join('{:{}}'.format(item, col_widths[i])
                                                    for i, item in enumerate(line)) + ' |')
        formatted_table = '\n'.join(complete_table)
        return formatted_table

    @classmethod
    def _validate_table_input(cls, headers, rows):
        """Validate table input by checking that headers and rows are set
        and each are a valid list and correct length.
        """
        if not headers or not isinstance(headers, list):
            raise ValueError(
                'Headers are either not set or are not a proper array.'
            )
        elif not rows or not isinstance(rows, list):
            raise ValueError(
                'Rows are either not set or are not a proper array.'
            )

        table_length = len(headers)
        for i, row in enumerate(rows):
            if not isinstance(row, list):
                raise IndexError(
                    f'Row {i + 1} is not a proper array.'
                )
            row_length = len(row)
            if row_length != table_length:
                raise IndexError(
                    f'Row {i + 1} has {row_length} columns which doesn\'t match the table columns of {table_length}.'
                )

        return True
