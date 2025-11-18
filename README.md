<div align="center">

# Pretty Tables

Create pretty tables from headers and rows, perfect for console output.

[![Build Status](https://github.com/Justintime50/pretty-tables/workflows/build/badge.svg)](https://github.com/Justintime50/pretty-tables/actions)
[![Coverage Status](https://img.shields.io/codecov/c/github/justintime50/pretty-tables)](https://app.codecov.io/github/Justintime50/pretty-tables)
[![PyPi](https://img.shields.io/pypi/v/pretty-tables)](https://pypi.org/project/pretty-tables/)
[![Licence](https://img.shields.io/github/license/justintime50/pretty-tables)](LICENSE)

<img src="https://raw.githubusercontent.com/justintime50/assets/main/src/pretty-tables/showcase.png" alt="Showcase">

</div>

Pretty Tables will create uniformly dispersed columns based on the input given and can be scaled to your needs in length of the table or number of columns. The input is automatically validated and allows for custom formatting making generating Pretty Tables a breeze.

## Install

```bash
# Install package
pip3 install pretty-tables

# Install locally
just install
```

## Usage

Pretty Tables is simple to use. Create a table by calling `pretty_tables.create()`, pass a list of headers and a 2 dimensional list of rows (each row must match the length of the headers). Pass an optional `empty_cell_placeholder` string, `colors` list, or a `truthy` index to customize your Pretty Table.

Pretty Tables will automatically validate the input and convert each item to a string before returning successfully; however, you can pass Pretty Tables any data type within the header or row lists. In the following example, we are using `integers`, `booleans`, `None`, and `strings`:

```python
import pretty_tables

headers = ['ID', 'Name', 'Occupation', 'Employed']
rows = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]

# Add optional custom colors to each column
colors = [
    pretty_tables.Colors.red,
    pretty_tables.Colors.green,
    pretty_tables.Colors.blue,
    pretty_tables.Colors.purple,
]

# Generate the pretty table output
table = pretty_tables.create(
    headers=headers,
    rows=rows,
    empty_cell_placeholder='No data',  # Optional: override the default `None` with a custom string
    colors=colors,  # Optional: mutually exclusive with `truthy`
    # truthy=3,  # Optional: integer of the column you want to check for truthy values on, mutually exclusive with `colors`
)

print(table)
```

### Colors

You can also color each column differently by using the `colors` argument and passing a list of colors from the `pretty_tables.Colors` class. The input list must match the length of the headers list.

- black
- blue
- cyan
- green
- purple
- red
- white
- yellow
- bold
- reset (resets all text formatting)
- underline
- none (acts like reset, used instead of passing `None` as a color)

## Development

```bash
# Get a comprehensive list of development tools
just --list
```

## Attribution

- [Stack Overflow question on formatting tables for console](https://stackoverflow.com/a/8356620/865091)
